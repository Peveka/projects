from googletrans import Translator
import telebot
from telebot import types

token = ""
bot = telebot.TeleBot(token)
markup = types.ReplyKeyboardMarkup(one_time_keyboard = True)
en = types.KeyboardButton("en")
ru = types.KeyboardButton("ru")
translator = Translator()
markup.add(en, ru)

with open("lang.txt", "w", encoding="utf-8") as f:
    f.write("ru\n")
    f.write("en")

@bot.message_handler(commands=["start"])
def hello(message):
    bot.send_message(message.chat.id, "Привет! Введи текст для перевода. Режим перевода по умолчанию: с русского на английский, для смены, пропиши /language ")

@bot.message_handler(commands=["language"])
def langu(message):
    ask = bot.send_message(message.chat.id, "Выберите язык: ", reply_markup= markup)
    bot.register_next_step_handler(ask, change_lang)

def change_lang(message):
    if message.text == "en":
        with open("lang.txt", "w", encoding="utf-8") as f:
            f.write("en\n")
            f.write("ru")
    elif message.text == "ru":
        with open("lang.txt", "w", encoding="utf-8") as f:
            f.write("ru\n")
            f.write("en")

@bot.message_handler(content_types=["text"])
def trans(message):
    with open("lang.txt", "r", encoding="utf-8") as f:
        language = f.readlines()
    result = translator.translate(message.text, src = language[0][0:2], dest= language[1][0:2])
    bot.send_message(message.chat.id, result.text)

bot.polling()
