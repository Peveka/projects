import random
def prog(num, passw=''):
    letters = ("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz123456789_!@#$_[]")
    for i in range(num):
        a = random.randint(0, len(letters) - 1)
        let = letters[a]
        passw += let
    print(passw)
prog(num = int(input("Введите кол-во символов в пароле: ")))