import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from tgbot.config import load_config
from tgbot.filters.admin import AdminFilter
from tgbot.handlers.CaseVariant import register_case_variant
from tgbot.handlers.CaseWorker import register_case_worker
from tgbot.handlers.admin import register_admin
from tgbot.handlers.after_the_case import register_after_the_case
from tgbot.handlers.data_collection import register_data_collection
from tgbot.handlers.interaction_case import register_interaction_case
from tgbot.handlers.life_situation import register_live_situation_worker
from tgbot.handlers.password_write import register_password_write_worker
from tgbot.handlers.user import register_user
from tgbot.handlers.variant_case import register_variant_case
from tgbot.middlewares.environment import EnvironmentMiddleware
from tgbot.services.db import Database


logger = logging.getLogger(__name__)

#commit
def register_all_middlewares(dp, config):
    dp.setup_middleware(EnvironmentMiddleware(config=config))


def register_all_filters(dp):
    dp.filters_factory.bind(AdminFilter)


def register_all_handlers(dp):
    register_admin(dp)
    register_user(dp)

    register_data_collection(dp)
    register_case_worker(dp)
    register_live_situation_worker(dp)
    register_password_write_worker(dp)
    register_interaction_case(dp)
    register_variant_case(dp)
    register_after_the_case(dp)



async def main():
    logging.basicConfig(
        level=logging.INFO,
        format=u'%(filename)s:%(lineno)d #%(levelname)-8s [%(asctime)s] - %(name)s - %(message)s',
    )
    logger.info("Starting bot")
    config = load_config(".env")

    #storage = RedisStorage2() if config.tg_bot.use_redis else MemoryStorage()
    storage = MemoryStorage()
    bot = Bot(token=config.tg_bot.token, parse_mode='HTML')
    dp = Dispatcher(bot, storage=storage)

    bot['config'] = config

    register_all_middlewares(dp, config)
    register_all_filters(dp)
    register_all_handlers(dp)

    # start
    try:
        await dp.start_polling()
    finally:
        await dp.storage.close()
        await dp.storage.wait_closed()
        await bot.session.close()


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        logger.error("Bot stopped!")
