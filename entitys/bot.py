import telebot
from dotenv import load_dotenv, find_dotenv
from utils import welcome_message
from genres import genres
from entitys.parser import Request
load_dotenv(find_dotenv())

bot = telebot.TeleBot("6252209212:AAFW8AnZirrhTBi-4xveFL_l5Oqtg0FHPxI")


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, welcome_message())


@bot.message_handler()
def get_message(message):
    parser = Request()
    data = genres
    for ru, en in data.items():
        if message.text in ru:
            bot.send_message(message.chat.id, parser.movies_by_genres(en), parse_mode='html')

