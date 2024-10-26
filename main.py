from tkinter import *
import random
import time
import os

levels = ["E7FEF9","060270","53CC86","E13901","000055","FFFFFF","000000","160F3F"]
levelz = ["C5FFF4","04023E","01FCCA","C03203","000088","FFFFFF","000000","160F3F"]
colorz = ["FFFFFF","FFFFFF","000000","000000","0000FF","88FF88","00BBBB","00FF00"]
icon = ["⦵","⨴","⇗","⮽","Ʊ","↻","⭗","Ѫ"]
level = 0
goal = 500
a = Tk()
a.title("Clickvar")
a.config(bg='#'+levels[level])
x = 1

mini = 1
limit = 3

def c():
    global x
    global level
    global levels
    global goal
    global mini
    global limit

    if random.randrange(1,6) == 1:
        os.system('cls')
        print("Latest Entity\n========================")
        y = random.randrange(mini,limit)
        if y == 1:
            x += 50
            print("Name: Zeke\nAppearance = ;)\nModifier = +50")
        elif y == 2:
            x += 25
            print("Name: Bob\nAppearance = :)\nModifier = +25")
        elif y == 3:
            x += 10
            print("Name: Josh\nAppearance = :D\nModifier = +10")
        elif y == 4:
            x *= -1
            x = round(x)
            print("Name: Sareka\nAppearance = :P\nModifier = *-1.5")
        elif y == 5:
            x -= 33
            print("Name: Brad\nAppearance = >:}\nModifier = -33")
        elif y == 6:
            x *= 1.3
            x = round(x)
            print("Name: Lerp\nAppearance = :]\nModifier = *1.3")
        elif y == 7:
            x /= 1.1
            x = round(x)
            print("Name: Xleva\nAppearance = XD\nModifier = /1.1")
        elif y == 8:
            x *= -2
            print("Name: Lenna\nAppearance = XP\nModifier = *-1")
    else:
        x += 1
    if x >= goal:
        level += 1
        if level == 1:
            limit = 5
        elif level == 2:
            mini = 2
        elif level == 3:
            limit = 6
        elif level == 4:
            mini = 3
            limit = 7

        if level == len(levels):
            exit()
        a.config(bg='#'+levels[level])
        x = 0
        
    b.config(text=icon[level]+" "+str(x), bg='#'+levelz[level], activebackground='#'+levelz[level], fg='#'+colorz[level], activeforeground='#'+colorz[level])

b = Button(a, text="⦵ "+str(x), font=("Arial, 32"), command=c, bg='#'+levelz[level], activebackground='#'+levelz[level], fg='#'+colorz[level], activeforeground='#'+colorz[level])
b.place(relx=0.5, rely=0.5, anchor=CENTER)

a.state('zoomed')
a.mainloop()
