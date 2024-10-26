from tkinter import *
import random
import time

levels = ["E7FEF9","FF0000","00FF00","0000FF","FF00FF","FFFF00","00FFFF","FFFFFF"]
levelz = ["C5FFF4","FF3333","33FF33","3333FF","FF33FF","FFFF33","33FFFF","FFFFFF"]
colorz = ["FFFFFF","000000","000000","000000","000000","000000","000000","000000"]
level = 0
goal = 2^31
a = Tk()
a.title("Click to Start")
a.config(bg='#'+levels[level])
x = 1

def c():
    global x
    global level
    global levels
    global goal

    a.title("Clickval: Level " + str(level+1))
    if random.randrange(1,6) == 1:
        y = random.randrange(1,7)
        if y == 1:
            x += 50
        elif y == 2:
            x += 25
        elif y == 3:
            x += 10
        elif y == 4:
            x *= -1.5
            x = round(x)
        elif y == 5:
            x -= 33
        elif y == 6:
            x /= 1.1
            x = round(x)
        else:
            x *= -1
    else:
        x += 1
    if x >= goal:
        level += 1
        if level == len(levels):
            exit()
        a.config(bg='#'+levels[level])
        x = 0
        
    b.config(text="⦵"+str(x), bg='#'+levelz[level], activebackground='#'+levelz[level], fg='#'+colorz[level], activeforeground='#'+colorz[level])

b = Button(a, text="⦵"+str(x), font=("Arial, 32"), command=c, bg='#'+levelz[level], activebackground='#'+levelz[level], fg='#'+colorz[level], activeforeground='#'+colorz[level])
b.place(relx=0.5, rely=0.5, anchor=CENTER)

a.state('zoomed')
a.mainloop()
