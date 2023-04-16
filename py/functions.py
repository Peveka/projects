#from matplotlib import pyplot as plt
func = input("Введите тип вашей функции (Кв / Лин / Гип) ")


if func.lower == "кв":
    print("Вид функции y = ax**2+bx+c")
    a = int(input("Введите коэф. a "))
    b = int(input("Введите коэф. b "))
    c = int(input("Введите коэф. с "))
    vershinax = -b / 2 * a
    x = vershinax
    vershinay = a * x ** 2 + b * x + c
    vershina = (vershinax, vershinay)
    print(f"Вершина параболы: {vershina}")
    print("Точки для построения: ")
    for i in range(-3, 4):
        x = i
        func = a * x ** 2 + b * x + c
        y = func
        A = (x, y)
        #plt.plot(A)
        #plt.show()
        print(A)



elif func.lower == "лин":
    print("Вид фунции: y = kx+m")
    k = int(input("Введите коэф. k: "))
    m = int(input("Введите коэф. m: "))
    for i in range(0, 2):
        x = i
        y = k * x + m
        A = (x, y)
        print(A)


elif func.lower == "гип":
    print("Вид функции: y = k / x")
    k = int(input("Введите коэф k: "))
    if k == 0:
        print("k не может быть равен 0!")
    if k != 0:
        for i in range(-3, 0):
            x = i
            y = k / x
            a = (x, y)
            print(a)
        for i in range(1, 4):
            x = i
            y = k / x
            a = (x, y)
            print(a)

else:
    print("Такой функции нет!")