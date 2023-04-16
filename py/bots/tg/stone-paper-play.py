import random, telebot
from telebot import types

token = "6171477610:AAGL2KvYTDW-POF3gY6g8fJIqcoEtB3QW8E"
bot = telebot.TeleBot(token)

menu = types.ReplyKeyboardMarkup()
b1 = types.KeyboardButton(text = "/start")
b2 = types.KeyboardButton(text = "/help")
b3 = types.KeyboardButton(text = "ножницы")
b4 = types.KeyboardButton(text = "бумага")
b5 = types.KeyboardButton(text = "камень")

menu.add(b1,b2,b3,b4,b5)

@bot.message_handler(commands=["help"])
def help(message):
    bot.send_message(message.chat.id, "Это игра камень/ножницы/бумага, чтобы начать, напишите /start")


@bot.message_handler(commands=["start"])
def ask(message):
    text = bot.send_message(message.chat.id, "Выберите чем будете играть (камень, ножницы, бумага): ", reply_markup=menu)
    bot.register_next_step_handler(text, ans)

def ans(message):
    player_choice = message.text.lower()
    lst = ["камень", "ножницы", "бумага"]
    bot_choice = random.choice(lst)
    bot.send_message(message.chat.id, f"Бот выбрал: {bot_choice}", reply_markup=menu)
    if bot_choice == player_choice:
        bot.send_message(message.chat.id, "Ничья!", reply_markup=menu)
    elif bot_choice == "камень" and player_choice == "ножницы":
        bot.send_message(message.chat.id, "Победил бот!", reply_markup=menu)
    elif bot_choice == "бумага" and player_choice == "ножницы":
        bot.send_message(message.chat.id, "Вы победили!", reply_markup=menu)
    elif bot_choice == "ножницы" and player_choice == "бумага":
        bot.send_message(message.chat.id, "Победил бот!", reply_markup=menu)
    elif bot_choice == "камень" and player_choice == "бумага":
        bot.send_message(message.chat.id, "Победил пользователь!", reply_markup=menu)
    elif bot_choice == "ножницы" and player_choice == "камень":
        bot.send_message(message.chat.id, "Вы победили!", reply_markup=menu)
    elif bot_choice == "бумага" and player_choice == "камень":
        bot.send_message(message.chat.id, "Победил бот!", reply_markup=menu)


bot.polling(none_stop=True, interval=0)