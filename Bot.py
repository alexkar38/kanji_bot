import telebot
import settings
import json
import requests


bot = telebot.TeleBot(settings.TELEGRAMM_TOKEN)

@bot.message_handler(content_types=['text'])

def start(message):    
    try:
        url = f'https://kanjiapi.dev/v1/kanji/{message.text}'
        response = requests.get(url).json() 
        answer = response['meanings']      
             
    except Exception:
        answer = "error:"     
    print(answer)    
    print (response)       
    bot.send_message(message.chat.id, answer, parse_mode='html')


bot.polling(none_stop=True)
