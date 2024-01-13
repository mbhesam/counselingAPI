import logging
from telegram.ext import ApplicationBuilder, PicklePersistence
from .handlers import main_handler
from moshavereAPI.settings import BOT_TOKEN, HTTP_PROXY, REQUEST_TIME_OUT

BOT_NAME = 'hashem_crawler'

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.DEBUG,
)

if __name__ == '__main__':
    persistence = PicklePersistence(filepath='hashem_bot/bin/conversations')
    application = ApplicationBuilder().token(
        BOT_TOKEN
    ).get_updates_proxy_url(
        HTTP_PROXY
    ).proxy_url(
        HTTP_PROXY
    ).persistence(persistence).build()
    application.add_handler(main_handler)
    application.run_polling(
        timeout=REQUEST_TIME_OUT,
        pool_timeout=REQUEST_TIME_OUT,
        read_timeout=REQUEST_TIME_OUT,
        write_timeout=REQUEST_TIME_OUT,
        connect_timeout=REQUEST_TIME_OUT,
    )
