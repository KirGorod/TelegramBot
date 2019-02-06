import requests
import telebot
import os
import random
import math
import functions
import constants

from telebot.types import Message

TOKEN = constants.TOKEN

bot = telebot.TeleBot(TOKEN)



#Обработчик комманд
@bot.edited_message_handler(content_types=['text'])
@bot.message_handler(commands=['start','help', 'test'])
def comand_handler(message: Message):
    if '/help' in message.text:
        bot.reply_to(message, 'Help info')
    elif '/start' in message.text:
        bot.reply_to(message, 'Start info')
    elif '/test' in message.text:
        bot.reply_to(message, functions.print_emoji("Rain"))
    else:
        pass

#Команда погоды
@bot.edited_message_handler(content_types=['text'])
@bot.message_handler(commands=['weather'])
def command_weather(message):
    print(message.text)
    if(len(message.text.split())) < 2:
        bot.send_message(message.chat.id, functions.weather_payload())
    elif (len(message.text.split())) >= 2:
        City = message.text.split(sep = ' '); City = City[-1]
        if City.isdigit() == True:
            bot.reply_to(message, "Digits`s are not allowed!")
        else:
            City = message.text.split(sep = ' '); City = City[-1]
            bot.send_message(message.chat.id, functions.weather_payload(City))



bot.polling(timeout=60)