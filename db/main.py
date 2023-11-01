import asyncio

from orm import ORM


async def main() -> None:
    await ORM.create_tables()


if __name__ == "__main__":
    asyncio.run(main())
