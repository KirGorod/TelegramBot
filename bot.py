import requests
import telebot
import os
import pickle

from telebot.types import Message

TOKEN = "702003056:AAEN2ezPlR5hjTe1Bz6OiHLzNLUF8XUnZ9U"
STICKER = 'CAADAgADHwADaJpdDDUrtxkEhXY8Ag'
chat_id = '405732032'

bot = telebot.TeleBot(TOKEN)

def game():
    with open('data.pickle', 'rb') as f:
        data = pickle.load(f)
        return dict(data)
def weather():
    url= 'http://api.openweathermap.org/data/2.5/weather?appid=b785080d09ffe12ee852f2035e884903&q=Kiev'
    json_content = requests.get(url).json()
    json_content = json_content.pop("weather")
    json_content = json_content.pop()
    current_weather = json_content.pop("main")

    return str(current_weather)


@bot.edited_message_handler(content_types=['text'])
@bot.message_handler(commands=['start','help', 'weather', 'game'])
def comand_handler(message: Message):
    if '/help' in message.text:
        bot.reply_to(message, 'Help info')
    elif '/start' in message.text:
        bot.reply_to(message, 'About bot: ')
    elif '/weather' in message.text:
        current_weather = weather()
        bot.send_message(chat_id, current_weather)
    elif 'game' in message.text:
        data = game()
        print(data)
        bot.reply_to(message, str(data))
    else:
        pass


bot.polling(timeout=60)