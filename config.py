"""
Application configuration.

This module centralizes configuration values used throughout the project.
Environment variables are loaded from a .env file when available.
"""

from __future__ import annotations

import os
from dataclasses import dataclass

try:
    from dotenv import load_dotenv  # type: ignore
except Exception:  # pragma: no cover - fallback if python-dotenv is not installed
    def load_dotenv(*_args, **_kwargs):
        """Fallback no-op load_dotenv when python-dotenv is unavailable."""


# Load environment variables from .env (no-op if python-dotenv is not installed)
load_dotenv()


@dataclass(frozen=True)
class Settings:
    """
    Immutable application settings.
    """

    app_name: str
    app_version: str
    binance_base_url: str
    request_timeout: float


settings = Settings(
    app_name="AEGIS",
    app_version="0.1.0",
    binance_base_url=os.getenv(
        "BINANCE_BASE_URL",
        "https://api.binance.com",
    ),
    request_timeout=float(
        os.getenv(
            "REQUEST_TIMEOUT",
            "10",
        )
    ),
)