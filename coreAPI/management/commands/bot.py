from telegram.ext import ApplicationBuilder, PicklePersistence
from moshavereBOT.handlers import main_handler
#from moshavereAPI.settings import BOT_TOKEN, REQUEST_TIME_OUT, PROXY_URL
from django.core.management.base import BaseCommand, CommandError
import os

os.environ["DJANGO_ALLOW_ASYNC_UNSAFE"] = "true"


# class Command(BaseCommand):
#     persistence = PicklePersistence(filepath='conversations/conversations')
#     application = ApplicationBuilder().token(
#         BOT_TOKEN
#     ).get_updates_proxy_url(
#         PROXY_URL
#     ).proxy_url(
#         PROXY_URL
#     ).persistence(persistence).build()
#     application.add_handler(main_handler)
#     application.run_polling(
#         timeout=REQUEST_TIME_OUT,
#         pool_timeout=REQUEST_TIME_OUT,
#         read_timeout=REQUEST_TIME_OUT,
#         write_timeout=REQUEST_TIME_OUT,
#         connect_timeout=REQUEST_TIME_OUT,
#     )
