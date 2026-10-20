# -*- coding: utf-8 -*-
"""Stub: Max bot отключён в photo-only handoff."""
from __future__ import annotations
from pathlib import Path
from typing import Any


def list_user_projects(projects_dir: Path, user_id: str, *, limit: int = 5) -> list[dict[str, Any]]:
    return []


def consume_bridge_token(cloud_dir: Path, token: str) -> dict[str, Any] | None:
    return None


def handle_update(cloud_dir: Path, projects_dir: Path, upd: dict) -> None:
    return None
