import telebot


bot = telebot.TeleBot('6252209212:AAFW8AnZirrhTBi-4xveFL_l5Oqtg0FHPxI')


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Привет')


if __name__ == '__main__':
    bot.polling(none_stop=True)
