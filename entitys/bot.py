import telebot
from utils import welcome_message

bot = telebot.TeleBot('6252209212:AAFW8AnZirrhTBi-4xveFL_l5Oqtg0FHPxI')


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, welcome_message())

