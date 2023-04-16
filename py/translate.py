from googletrans import Translator
translator = Translator()
film = input("Введите название фильма: ")
lang = input("Введите код языка: ")
result = translator.translate(film, src = "ru", dest = lang)
print(result.text)
