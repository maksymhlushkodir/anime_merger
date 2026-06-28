import click
from anime_merger.analyzer import parse_anime_file
from anime_merger.merger import merge_anime_files


@click.command()
@click.argument("base_file")
@click.argument("input_files", nargs=-1)
@click.option("--output", default="output.mkv")
def main(base_file, input_files, output):
    anime_files = [
        parse_anime_file(base_file)
    ]

    for file in input_files:
        anime_files.append(
            parse_anime_file(file)
        )
    merge_anime_files(
        anime_files,
        output
    )

if __name__ == "__main__":
    main()