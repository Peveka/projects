from gtts import gTTS
import telebot
from telebot import types

token = "6171477610:AAGL2KvYTDW-POF3gY6g8fJIqcoEtB3QW8E"
bot = telebot.TeleBot(token)
markup = types.ReplyKeyboardMarkup(one_time_keyboard = True)
en = types.KeyboardButton("en")
ru = types.KeyboardButton("ru")
markup.add(en, ru)

with open("lang.txt", "w", encoding="utf-8") as f:
    f.write("ru")

@bot.message_handler(commands=["start"])
def hello(message):
    bot.send_message(message.chat.id, "Привет! Введи текст для озвучки\n P.s. язык озвучки по умолчанию русский, для смены, пропиши /language ")

@bot.message_handler(commands=["language"])
def langu(message):
    ask = bot.send_message(message.chat.id, "Выберите язык: ", reply_markup= markup)
    bot.register_next_step_handler(ask, change_lang)

def change_lang(message):
    if message.text == "en":
        with open("lang.txt", "w", encoding="utf-8") as f:
            f.write("en")
    elif message.text == "ru":
        with open("lang.txt", "w", encoding="utf-8") as f:
            f.write("ru")

@bot.message_handler(content_types=["text"])
def voice(message):
    with open("lang.txt", "r", encoding="utf-8") as f:
        language = f.read()
    result = gTTS(text = message.text, lang = language, slow = False)
    result.save("voice.mp3")
    with open("voice.mp3", "rb") as f:
        audio = f.read()
    bot.send_audio(message.chat.id, audio)

bot.polling()
