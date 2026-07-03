import asyncio

from api.binance_rest import BinanceRestClient


async def main() -> None:
    client = BinanceRestClient()

    try:
        price = await client.get_symbol_price("BTCUSDT")
        print(f"BTCUSDT Price: {price}")
    finally:
        await client.close()


asyncio.run(main())