"""
Entry point for Project AEGIS.
"""

from __future__ import annotations

import asyncio

from rich.console import Console
from rich.table import Table

from api.binance_rest import BinanceRestClient

console = Console()


async def main() -> None:
    """
    Run the AEGIS terminal.
    """
    console.rule("[bold cyan]Project AEGIS[/bold cyan]")

    client = BinanceRestClient()

    try:
        price = await client.get_symbol_price("BTCUSDT")

        table = Table(title="Live Market Data")
        table.add_column("Symbol", style="cyan")
        table.add_column("Price (USDT)", justify="right", style="green")

        table.add_row("BTCUSDT", f"{price:,.2f}")

        console.print(table)

    finally:
        await client.close()

    console.print("\n[bold green]Sprint 1 completed successfully![/bold green]")


if __name__ == "__main__":
    asyncio.run(main())