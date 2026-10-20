# -*- coding: utf-8 -*-
"""Stub: video pipeline отключён в photo-only handoff."""
from __future__ import annotations
from pathlib import Path


DEFAULT_VIDEO_MODEL = ""
DEFAULT_VIDEO_DURATION = 5
DEFAULT_VIDEO_RESOLUTION = "480p"
PHOTO_OVERVIEW_PROMPT = ""
CLIP_RELIGHT_PROMPT = ""


def video_model() -> str:
    return ""


def has_ffmpeg() -> bool:
    return False


def ffmpeg_bin() -> str:
    return "ffmpeg"


def run_image_to_video(*args, **kwargs):
    raise RuntimeError("Video disabled in photo-only package")


def run_clip_relight(*args, **kwargs):
    raise RuntimeError("Video disabled in photo-only package")


def trim_video(src: Path, dst: Path, *, seconds: float = 8.0) -> Path:
    raise RuntimeError("Video disabled in photo-only package")


def concat_before_after(before: Path, after: Path, out: Path) -> Path:
    raise RuntimeError("Video disabled in photo-only package")
