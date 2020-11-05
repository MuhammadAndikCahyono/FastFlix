# -*- coding: utf-8 -*-
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Union, List
from tempfile import TemporaryDirectory

from appdirs import user_data_dir
from box import Box

from fastflix.models.base import BaseDataClass

from fastflix.models.encode import AudioTrack, SubtitleTrack, x265Settings


@dataclass
class VideoSettings(BaseDataClass):
    crop: Union[str, None] = None
    start_time: Union[float, int] = 0
    end_time: Union[float, int] = 0
    fast_seek: bool = True
    rotate: Union[str, None] = None
    vertical_flip: bool = False
    horizontal_flip: bool = False
    remove_metadata: bool = True
    copy_chapters: bool = True
    video_title: str = ""
    selected_track: int = 0
    output_path: Path = None
    scale: Union[str, None] = None
    ffmpeg_extra: str = ""
    video_encoder_settings: Union[x265Settings] = None
    audio_tracks: List[AudioTrack] = field(default_factory=list)
    subtitle_tracks: List[SubtitleTrack] = field(default_factory=list)
    conversion_commands: List = field(default_factory=list)


@dataclass
class Status(BaseDataClass):
    success: bool = False
    error: bool = False
    complete: bool = False
    running: bool = False
    current_command: int = 0


@dataclass
class Video(BaseDataClass):
    source: Path
    width: int = 0
    height: int = 0
    duration: Union[float, int] = 0
    streams: Box = None

    work_path: TemporaryDirectory = None
    pix_fmt: str = ""
    format: Box = None

    # Color Range Details
    color_space: str = ""
    color_primaries: str = ""
    color_transfer: str = ""

    # HDR10 Details
    master_display: Box = None
    cll: str = ""

    video_settings: VideoSettings = field(default_factory=VideoSettings)
    status: Status = field(default_factory=Status)
