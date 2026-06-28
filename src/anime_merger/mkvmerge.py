import json
import subprocess
from shutil import which


def find_mkvmerge():
    mkvmerge_path = which("mkvmerge")
    if mkvmerge_path is None:
        raise RuntimeError(
            'Error: Program "mkvmerge" not found. Please install it before using the script'
        )

    return mkvmerge_path

def run_mkvmerge(command: list[str]) -> str:
    result = subprocess.run(
        command,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        encoding="utf-8"
    )

    if result.returncode != 0:
        raise RuntimeError(
            f'mkvmerge failed with code {result.returncode}. Error: {result.stderr}'
        )

    return result.stdout

def get_file_info(mkvmerge_path: str, file_path: str) -> dict:
    command = [
        mkvmerge_path,
        '-J',
        file_path
    ]

    stdout = run_mkvmerge(command)

    return json.loads(stdout)


