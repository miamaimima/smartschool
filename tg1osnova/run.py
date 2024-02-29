import asyncio
from aiogram import Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage

from src.handlers import start, registra, mned
from src.handlers import profile, projectinfo, myrebenok
from src.misc import bot, logger






# Запуск бота
async def main():
    print(123)
    dp = Dispatcher(storage=MemoryStorage())
    dp.include_routers(
        myrebenok.router,
        projectinfo.router,
        mned.router,
        start.router,
        profile.router,
        registra.router
    )
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)






if __name__ == "__main__":
    logger.info('Бот запущен')
    asyncio.run(main())
