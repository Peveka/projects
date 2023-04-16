import telebot
import requests
from datetime import datetime

#p.s. на сайте с погодой данные хуйня, сильное отличие от гисметео и я.погоды

token = "6171477610:AAGL2KvYTDW-POF3gY6g8fJIqcoEtB3QW8E"
bot = telebot.TeleBot(token)
api = "63e3831ab77214770681c9b05485360b"

@bot.message_handler(commands=["start", "help"])
def start(message):
    mes = bot.send_message(message.chat.id, "Привет! Для того, чтобы узнать погоду в городе, введи его название.")
    bot.register_next_step_handler(mes, weather)

def weather(message):
    city = message.text.strip().lower()
    link = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api}&units=metric"
    try:
        r = requests.get(link)
        res = r.json()
        t1 = int(res['sys']['sunrise'])
        t2 = int(res['sys']['sunset'])
        t1 = datetime.utcfromtimestamp(t1).strftime('%D %H:%M')
        t2 = datetime.utcfromtimestamp(t2).strftime('%D %H:%M')
        bot.reply_to(message, f"""Погода сейчас: 
Температура сейчас: {res['main']['temp']} °C
Скорость ветра: {res['wind']['speed']} м/с
Облачность: {res['clouds']['all']} %
Время восхода: {t1} 
Время захода: {t2}
    """)
    except Exception:
        bot.reply_to(message, "Такого города нет!")


bot.polling(none_stop=True)