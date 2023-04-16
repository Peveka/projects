def counter(cnt_of_items, cnts = [], items = []):
    for i in range(cnt_of_items):
        global cnts, items
        item = input("Введите название продукта: ")
        cnt = input("Введите количество этого продукта: ")
        items.append(item)
        cnts.append(cnt)
        

def ticket(cnt_of_items):
    print("""------------------Кассовый чек:------------------""")
    for i in range(len(items)):
        print(f"№{i+1}: {items[i]} в количестве {cnts[i]}, на общую сумму {int(cnts[i])*99}")
    print(f"Общая сумма покупки: {cnt_of_items * 99}\nБудем рады видеть Вас снова!")

def buy(cnt_of_items):
    counter(cnt_of_items)
    ticket(cnt_of_items)

buy(cnt_of_items = int(input("Приветствуем Вас в магазине 10очка! Введите количество купленного товара: ")))


    