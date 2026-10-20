# -*- coding: utf-8 -*-
"""Stub: Max auth отключён в photo-only handoff."""
from __future__ import annotations
from pathlib import Path
from typing import Any


def bot_token() -> str:
    return ""


def bot_username() -> str:
    return ""


def bot_startapp_url(start_param: str = "auth") -> str:
    return ""


def bot_login_url(*, next_path: str = "/") -> str:
    return ""


def validate_init_data(init_data: str, *, max_age_sec: int = 86400) -> dict[str, Any]:
    raise ValueError("MAX auth disabled in photo-only package")


def load_users(cloud_dir: Path) -> dict[str, dict]:
    return {}


def upsert_user(cloud_dir: Path, payload: dict[str, Any]) -> dict:
    raise RuntimeError("MAX auth disabled in photo-only package")


def issue_session_token(max_user_id: str, *, ttl_sec: int = 1) -> str:
    return ""


def verify_session_token(token: str) -> str | None:
    return None
