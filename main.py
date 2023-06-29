import telebot
import openai
from googletrans import Translator

tb = telebot.TeleBot('5641540856:AAEjjtB9KjY179-6WRO2lIrv06CDPcMR8wE')
hello_msg = """
<b>Hello! You are now entered the bot!</b>
This bot created for talking with chatGPT
right from the <b>Telegram!</b>
"""
openai.api_key = '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'
tr = Translator()


@tb.message_handler(commands=['start'])
def hello(msg):
    tb.send_message(msg.chat.id, hello_msg, parse_mode='html')


@tb.message_handler(content_types=['text'])
def translate(msg):
    user_text = msg.text
    trans_text = tr.translate(user_text, dest='en')
    print(trans_text.text)

    response = openai.Completion.create(
        engine='text-davinci-003',
        prompt=trans_text.text,
        max_tokens=600,
        temperature=0.7
    )
    res = response.choices[0].text.strip()
    trans_res = tr.translate(res, dest='ru')

    tb.send_message(msg.chat.id, trans_res.text)



tb.polling(none_stop=True)