import telebot
import settings


bot = telebot.TeleBot(settings.TELEGRAMM_TOKEN)

@bot.message_handler(commands=['start'])

def start(message):
    bot.send_message(message.chat.id, 'こんにちわ')


bot.polling(none_stop=True)

