from dataclasses import dataclass

@dataclass
class StreamInfo:
    index: int
    codec: str
    stream_type: str
    language: str | None


@dataclass
class AnimeFile:
    path: str
    video_streams: list[StreamInfo]
    audio_streams: list[StreamInfo]
    subtitle_streams: list[StreamInfo]
