import telebot
import openai
from googletrans import Translator

tb = telebot.TeleBot('5641540856:AAEjjtB9KjY179-6WRO2lIrv06CDPcMR8wE')
hello_msg = """
<b>Hello! You are now entered the bot!</b>
This bot created for talking with chatGPT
right from the <b>Telegram!</b>
"""
openai.api_key = 'Enter_your_openai_api_key'
tr = Translator()

def split_text(text, max_tokens):
    words = text.split()
    segments = []
    current_segment = ""
    current_length = 0

    for word in words:
        if current_length + len(word.split()) <= max_tokens:
            current_segment += word + " "
            current_length += len(word.split())
        else:
            segments.append(current_segment.strip())
            current_segment = word + " "
            current_length = len(word.split())

    if current_segment:
        segments.append(current_segment.strip())

    return segments

@tb.message_handler(commands=['start'])
def hello(msg):
    tb.send_message(msg.chat.id, hello_msg, parse_mode='html')

@tb.message_handler(content_types=['text'])
def translate(msg):
    user_text = msg.text
    segments = split_text(user_text, 50)
    for segment in segments:
        trans_text = tr.translate(segment, dest='en').text
        response = openai.Completion.create(engine="text-davinci-003", prompt=trans_text, max_tokens=150)
        tb.send_message(msg.chat.id, response.choices[0].text.strip())

tb.polling(none_stop=True)
