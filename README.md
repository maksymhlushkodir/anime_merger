# Anime Merger

Merge audio tracks and subtitles from multiple anime releases into a single MKV file.

## Features

- Merge audio tracks
- Merge subtitle tracks
- Preserve original video
- Built on mkvmerge

## Requirements

- Python 3.11+
- MKVToolNix (`mkvmerge` must be available in PATH)

## Installation

```bash
pip install -e .
```

## Usage

```bash
anime-merger base.mkv english.mkv italian.mp4
```

Output:

```
output.mkv
```