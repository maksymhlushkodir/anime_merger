from anime_merger.mkvmerge import run_mkvmerge
from anime_merger.mkvmerge import find_mkvmerge
from anime_merger.models import AnimeFile


def merge_anime_files(
        anime_files: list[AnimeFile],
        output: str) -> None:
    mkvmerge_path = find_mkvmerge()

    command = [
        mkvmerge_path,
        '-o',
        output,
        anime_files[0].path,
    ]

    for file in anime_files[1:]:
        command.extend([
            file.path,
            '--no-video'
        ])

    run_mkvmerge(command)