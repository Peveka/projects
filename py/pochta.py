import smtplib
import mimetypes
from email.mime.text import MIMEText
from pyfiglet import Figlet
from tqdm import tqdm
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
def send_email():
    sender = "" #ПОЧТА | ПЕРЕД ОТПРАВКОЙ НЕ ЗАБЫТЬ ВЫКЛЮЧИТЬ ПРОВЕРКУ НА БОТА
    password = "" #ПАРОЛЬ ОТ ПОЧТЫ ОТПРАВИТЕЛЯ
    recipient = "" #ПОЛУЧАТЕЛЬ

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()

    #try:
    #    with open ("Базаданных.txt") as file:
    #        recipient = file.read()
    #except IOError:
    #    return "Ошибка базы данных почт"

    try:
        with open("text.html") as file:
            template = file.read()
    except IOError:
        return "Файл с текстом не распознается!"

    try:
        server.login(sender, password)
        # msg = MIMEText(template, "html")
        msg = MIMEMultipart()
        msg["From"] = sender
        msg["To"] = recipient
        msg["Subject"] = "" #ТЕМА ПИСЬМА

        #msg.attach(MIMEText("Hello world"))
        msg.attach(MIMEText(template, "html"))
        #with open("Распродажа.jpg", "rb") as f:
        #    file = MIMEImage(f.read())

        #file.add_header("content-disposition", "attachment", filename="Распродажа.jpg")
        #msg.attach(file)

        server.sendmail(sender, recipient, msg.as_string())

        return "Сообщение отправлено успешно!"
    except Exception as _ex:
        return f"{_ex}\n Проверьте введнные данные!"

def main():
    font_text = Figlet(font="slant")
    print(font_text.renderText("Отправка сообщений"))
    print(send_email())

if __name__ == "__main__":
    main()
