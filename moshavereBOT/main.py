import logging

from telegram.ext import ApplicationBuilder, PicklePersistence

from .handlers import main_handler

from decouple import config, Csv

BOT_NAME = 'hashem_crawler'

TELEGRAM_BOT_TOKEN = config('TELEGRAM_BOT_TOKEN')
TELEGRAM_BOT_WHITELIST_USERNAMES = config('TELEGRAM_BOT_WHITELIST_USERNAMES', cast=Csv(), default=',')
TELEGRAM_BOT_PROXY = config('TELEGRAM_BOT_PROXY')
TELEGRAM_BOT_REQUESTS_TIMEOUT = config('TELEGRAM_BOT_REQUESTS_TIMEOUT', cast=int, default=300)

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.DEBUG,
)

if __name__ == '__main__':
    persistence = PicklePersistence(filepath='hashem_bot/bin/conversations')
    application = ApplicationBuilder().token(
        TELEGRAM_BOT_TOKEN
    ).get_updates_proxy_url(
        TELEGRAM_BOT_PROXY
    ).proxy_url(
        TELEGRAM_BOT_PROXY
    ).persistence(persistence).build()
    application.add_handler(main_handler)
    application.run_polling(
        timeout=TELEGRAM_BOT_REQUESTS_TIMEOUT,
        pool_timeout=TELEGRAM_BOT_REQUESTS_TIMEOUT,
        read_timeout=TELEGRAM_BOT_REQUESTS_TIMEOUT,
        write_timeout=TELEGRAM_BOT_REQUESTS_TIMEOUT,
        connect_timeout=TELEGRAM_BOT_REQUESTS_TIMEOUT,
    )
