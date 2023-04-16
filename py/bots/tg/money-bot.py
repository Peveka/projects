import telebot
from currency_converter import CurrencyConverter
from telebot import types

token = "6171477610:AAGL2KvYTDW-POF3gY6g8fJIqcoEtB3QW8E"
bot = telebot.TeleBot(token)
conv = CurrencyConverter()
kb = types.InlineKeyboardMarkup()
b1 = types.InlineKeyboardButton(text="USD-EUR", callback_data="USD-EUR")
b2 = types.InlineKeyboardButton(text="EUR-USD", callback_data="EUR-USD")
b3 = types.InlineKeyboardButton(text="RUB-USD", callback_data="RUB-USD")
b4 = types.InlineKeyboardButton(text="USD-RUB", callback_data="USD-RUB")
b5 = types.InlineKeyboardButton(text="Другая валюта", callback_data="another")
kb.row(b1,b2)
kb.row(b3,b4)
kb.row(b5)
amount = 0

@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(message.chat.id, "Привет! Я бот-конвертор валют. Введите сумму денежных средств в исходной валюте: ")
    bot.register_next_step_handler(message, change)

def change(message):
    global amount
    try:
        amount = int(message.text.strip())
        bot.send_message(message.chat.id, "Выберите валюту из списка", reply_markup=kb)
    except ValueError:
        bot.send_message(message.chat.id, "Вы ввели неверное число!")
        bot.register_next_step_handler(message, change)
        return

@bot.callback_query_handler(func = lambda call: True)
def value(call):
    if amount > 0 and call.data != "another":
        values = call.data.upper().split('-')
        res = conv.convert(amount, values[0], values[1])
        bot.send_message(call.message.chat.id, f"Получается {round(res,2)}.")

    elif call.data == "another":
        bot.register_next_step_handler(bot.send_message(call.message.chat.id, "Укажите свою пару в формате:\nИСХОДНАЯ-НУЖНАЯ валюта (Пример: USD-EUR)"), another)

def another(message):
    values = message.text.upper().split('-')
    res = conv.convert(amount, values[0], values[1])
    bot.send_message(message.chat.id, f"Получается {round(res, 2)}.")


bot.polling(none_stop=True, interval=0)