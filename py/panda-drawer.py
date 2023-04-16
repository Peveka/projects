import turtle
 
sc = turtle.Screen()
sc.setup(640,640)
sc.title("Paint 2.0")
sc.bgcolor('pink')
 
# полоска меню
menu = turtle.Turtle()
menu.hideturtle()
menu.color('grey')
menu.shape('square')
menu.shapesize(2,50)
menu.penup()
menu.goto(0,280)
menu.showturtle()
 
# фон инструмента кисть
br_bg = turtle.Turtle()
br_bg.hideturtle()
br_bg.color('white')
br_bg.penup()
br_bg.shape('square')
br_bg.shapesize(2,4)
br_bg.goto(0,280)
br_bg.showturtle()
 
# надпись кисть
br_txt = turtle.Turtle()
br_txt.hideturtle()
br_txt.color('black')
br_txt.shape('square')
br_txt.shapesize(1)
br_txt.penup()
br_txt.goto(0,270)
br_txt.pendown()
br_txt.write('Кисть' , align = 'center' , font = ('Аrial' , 14
, 'bold'))
br_txt.penup()
br_txt.goto(0,270)
 
# кисть
brush = turtle.Turtle()
brush.speed(0)
brush.shape('square')
brush.shapesize(1)
brush.penup()
brush.goto(0,260)
brush.pendown()
brush.showturtle()
 
# фон инструмента ластик
er_bg = turtle.Turtle()
er_bg.hideturtle()
er_bg.color('white')
er_bg.penup()
er_bg.shape('square')
er_bg.shapesize(2,4)
er_bg.goto(100,280)
er_bg.showturtle()
 
# надпись ластик
er_txt = turtle.Turtle()
er_txt.hideturtle()
er_txt.color('black')
er_txt.penup()
er_txt.shape('square')
er_txt.shapesize(1)
er_txt.goto(100,270)
er_txt.pendown()
er_txt.write('Ластик' , align = 'center' , font = ('Аrial' ,
14 , 'bold'))
er_txt.penup()
er_txt.goto(50,270)
 
# ластик
ers = turtle.Turtle()
ers.speed(0)
ers.color('pink','cyan')
ers.pensize(10)
ers.shape('circle')
ers.shapesize(1)
ers.penup()
ers.goto(100,260)
ers.pendown()
ers.showturtle()
 
# размер пера фон кнопки 1
p2f = turtle.Turtle()
p2f.hideturtle()
p2f.color('white')
p2f.penup()
p2f.shape('square')
p2f.shapesize(2,2,0)
p2f.goto(-350,280)
p2f.showturtle()
 
# размер пера надпись и кнопка 1
p2 = turtle.Turtle()
p2.hideturtle()
p2.penup()
p2.goto(-350,275)
p2.pendown()
p2.shape('square')
p2.shapesize(0.5)
p2.color('black')
p2.write('2' , align = 'center' , font = ('Аrial' , 14 ,
'bold'))
p2.penup()
p2.goto(-350,270)
p2.showturtle()
 
# размер пера фон кнопки 2
p10f = turtle.Turtle()
p10f.hideturtle()
p10f.color('white')
p10f.penup()
p10f.shape('square')
p10f.shapesize(2,2,0)
p10f.goto(-300,280)
p10f.showturtle()
 
# размер пера надпись и кнопка 2
p10 = turtle.Turtle()
p10.hideturtle()
p10.penup()
p10.goto(-300,275)
p10.pendown()
p10.shape('square')
p10.shapesize(0.5)
p10.color('black')
p10.write('10' , align = 'center' , font = ('Аrial' , 14 ,
'bold'))
p10.penup()
p10.goto(-300,270)
p10.showturtle()
 
 
 
# кнопки цветов
c1 = turtle.Turtle()
c1.hideturtle()
c1.color('green')
c1.shape('square')
c1.shapesize(2,2,1)
c1.penup()
c1.goto(350,280)
c1.showturtle()
 
c2 = turtle.Turtle()
c2.hideturtle()
c2.color('red')
c2.shape('square')
c2.shapesize(2,2,1)
c2.penup()
c2.goto(300,280)
c2.showturtle()
 
c3 = turtle.Turtle()
c3.hideturtle()
c3.color('blue')
c3.shape('square')
c3.shapesize(2,2,1)
c3.penup()
c3.goto(400,280)
c3.showturtle()
 
 
#перемещение мышкой
def drag(x,y):
    brush.ondrag(None)
    brush.setheading(brush.towards(x,y))
    brush.goto(x,y)
    brush.ondrag(drag)
 
def drag_ers(x,y):
    ers.ondrag(None)
    ers.setheading(ers.towards(x,y))
    ers.goto(x,y)
    ers.ondrag(drag_ers)
 
#выбор цвета
def clickgreen(x,y):
    brush.color('green')
 
def clickred(x,y):
    brush.color('red')
 
def clickblue(x,y):
    brush.color('blue')
 
#выбор размера
def size2(x,y):
    brush.pensize(2)
 
def size10(x,y):
    brush.pensize(10)
 
 
brush.ondrag(drag, 1)
ers.ondrag(drag_ers, 1)
c1.onclick(clickgreen, 1)
c2.onclick(clickred,1)
c3.onclick(clickblue,1)
p2.onclick(size2, 1)
p10.onclick(size10, 1)
 
turtle.mainloop()