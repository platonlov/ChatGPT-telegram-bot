import telebot
import openai
from googletrans import Translator

tb = telebot.TeleBot('5641540856:AAEjjtB9KjY179-6WRO2lIrv06CDPcMR8wE')
hello_msg = """
<b>Hello! You are now entered the bot!</b>
This bot created for talking with chatGPT
right from the <b>Telegram!</b>
"""
openai_api_key = 'Enter_your_openai_api_key'
tr = Translator()


@tb.message_handler(commands=['start'])
def hello(msg):
    tb.send_message(msg.chat.id, hello_msg, parse_mode='html')


@tb.message_handler(content_types=['text'])
def translate(msg):
    user_text = msg.text
    trans_text = tr.translate(user_text, dest='en')
    print(trans_text.text)



tb.polling(none_stop=True)