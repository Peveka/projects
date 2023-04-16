import telebot

token = "6171477610:AAGL2KvYTDW-POF3gY6g8fJIqcoEtB3QW8E"
bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id,
                     "Привет! Я бот - помощник на день. Ты можешь писать мне свои задачи, а я буду помнить их до того момента, пока ты их не выполнишь! (для подробной информации пропиши /help)", )


@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id,
                     "Команды бота:\n/add - добавить новую задачу\n/remove - удалить задачу\n/check - посмотреть список задач на день")


@bot.message_handler(commands=['add'])
def add(message):
    text = bot.send_message(message.chat.id, "Напишите задачу, которую хотите добавить в список на день: ")
    bot.register_next_step_handler(text, add2)


def add2(message):
    file_name = str(message.from_user.id) + ".txt"
    with open(file_name, "a", encoding="utf-8") as f:
        f.write(message.text + "\n")
    bot.send_message(message.chat.id, "Задача успешно добавлена!")


@bot.message_handler(commands=['check'])
def chck(message):
    bot.send_message(message.chat.id, "Вы не выполнили следующие задачи: ")
    file_name = str(message.from_user.id) + ".txt"
    lst = open(file_name, "r", encoding="utf-8").readlines()
    ans = ''
    for j in lst:
        ans = ans + str(lst.index(j) + 1) + '. ' + j
    bot.send_message(message.chat.id, str(ans))


@bot.message_handler(commands=['remove'])
def remove(message):
    text = bot.send_message(message.chat.id, "Выберите задачу, которую вы выполнили и укажите номер её строки.")
    bot.register_next_step_handler(text, rmv)


def rmv(message):
    file_name = str(message.from_user.id) + ".txt"
    with open(file_name, "r", encoding="utf-8") as f:
        lst = f.readlines()
    try:
        lst[int(message.text) - 1] = ""
        with open(file_name, "w", encoding="utf-8") as f:
            f.writelines(lst)
        bot.send_message(message.chat.id, "Задача успешно выполнена!")
    except Exception:
        bot.send_message(message.chat.id, "Такой задачи нет!")


bot.polling(none_stop=True, interval=0)
