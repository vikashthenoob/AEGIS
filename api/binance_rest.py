"""
Async Binance REST client for Project AEGIS.
"""

from __future__ import annotations

from typing import Any

import httpx

from config import settings
from utils.logger import get_logger

logger = get_logger(__name__)


class BinanceRestClient:
    """
    Minimal asynchronous client for Binance REST API.
    """

    def __init__(self) -> None:
        self._client = httpx.AsyncClient(
            base_url=settings.binance_base_url,
            timeout=settings.request_timeout,
        )

    async def get_symbol_price(self, symbol: str) -> float:
        """
        Get the latest price for a trading symbol.

        Args:
            symbol: Example: "BTCUSDT"

        Returns:
            Latest price as a float.

        Raises:
            httpx.HTTPError: If the request fails.
            ValueError: If the response is invalid.
        """
        logger.info("Fetching price for %s", symbol)

        response = await self._client.get(
            "/api/v3/ticker/price",
            params={"symbol": symbol},
        )

        response.raise_for_status()

        data: dict[str, Any] = response.json()

        return float(data["price"])

    async def close(self) -> None:
        """
        Close the HTTP client.
        """
        await self._client.aclose()