from anime_merger.models import AnimeFile
from anime_merger.models import StreamInfo
from anime_merger.mkvmerge import get_file_info
from anime_merger.mkvmerge import find_mkvmerge

# validate_duration()

def parse_tracks(info:dict) -> tuple[
    list[StreamInfo],
    list[StreamInfo],
    list[StreamInfo]
]:
    # lists to sort
    videos = []
    audios = []
    subtitles = []

    for track in info['tracks']:
        stream = StreamInfo(
            index=int(track['id']),
            stream_type=track['type'],
            codec=track['properties'].get('codec_id') or
                  track['properties'].get('codec', 'unknown'),
            language=track['properties'].get('language', 'und')
        )

        if stream.stream_type == "video":
            videos.append(stream)
        elif stream.stream_type == "audio":
            audios.append(stream)
        elif stream.stream_type == "subtitles":
            subtitles.append(stream)

    return videos, audios, subtitles

def parse_anime_file(path: str) -> AnimeFile:

    mkvmerge_path = find_mkvmerge()
    info = get_file_info(mkvmerge_path ,path)

    videos, audios, subtitles = parse_tracks(info)

    return AnimeFile(
        path=path,
        video_streams=videos,
        audio_streams=audios,
        subtitle_streams=subtitles,
    )

