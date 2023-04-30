import telebot
import settings
import requests

bot = telebot.TeleBot(settings.TELEGRAMM_TOKEN)

@bot.message_handler(content_types=['text'])

def start(message):
    url = f'https://kanjiapi.dev/v1/kanji/{message.text}'
    response = requests.get(url).json()
    #print(response)
    bot.send_message(message.chat.id, response)


bot.polling(none_stop=True)
