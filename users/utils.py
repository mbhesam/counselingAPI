from bs4 import BeautifulSoup
import jdatetime
import urllib.request
import telebot
from moshavereAPI.settings import BOT_TOKEN
import requests
from moshavereAPI.settings import REQUEST_PROXY

bot = telebot.TeleBot(BOT_TOKEN)

def check_platform_support(platform):
    if platform not in ['telegram', 'bale']:
        return False
    return True

def get_html(url, params=None):
    r = requests.get(url, params=params, proxies=REQUEST_PROXY)
    return r

def is_username_exists(username):
    url = f'https://t.me/{username}'
    html = get_html(url)
    source = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(source, 'lxml')
    if html.status_code == 200:
        if not len(soup.find_all('div', class_='tgme_page_additional')):
            result = False
        else:
            result = True
    else:
        result = 'Error'
    return result

