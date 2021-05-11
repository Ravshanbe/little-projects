import tb as tb

from transliterate import to_cyrillic, to_latin
import telebot

TOKEN = "1835645123:AAFiPJf75DjebP2smdGPGAkRZ2SH8NI-21I"
bot = telebot.TeleBot(TOKEN, parse_mode=None)


@bot.message_handler(commands=['start'])
def send_welcome(message):
    answer = 'Assalomu aleykum. Xush kelibsiz!'
    answer += '\nMatn kiriting'
    bot.reply_to(message, answer)


@bot.message_handler(func=lambda m: True)
def echo_all(message):
    msg = message.text
    answer = lambda msg: to_cyrillic(msg) if msg.isascii() else to_latin(msg)
    bot.reply_to(message, answer(msg))



bot.polling()
#
#
#
# text = input("Enter text:")
# if text.isascii():
#     print(to_cyrillic(text))
# else:
#     print(to_latin(text))
