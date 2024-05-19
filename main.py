import asyncio
from aiogram import Bot, Dispatcher, F

from app.handlers import router
from app.database.models import async_main



async def main():
    await async_main()
    bot = Bot(token='6545918505:AAE856yJouqGAsqwwhF8IUdFH24cbHwngAc')
    dispatcher = Dispatcher()
    dispatcher.include_router(router)
    await dispatcher.start_polling(bot)
    


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Exit')