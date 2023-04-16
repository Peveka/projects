from aiogram import Bot, Dispatcher, executor, types

bot = Bot("6171477610:AAGL2KvYTDW-POF3gY6g8fJIqcoEtB3QW8E")
dp = Dispatcher(bot)

executor.start_polling(dp)
