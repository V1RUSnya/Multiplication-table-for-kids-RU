import os
import random
from time import sleep
from tkinter import *

def cls():
    print("\n" * 100)

os.system("taskkill/IM explorer.exe /F")
sleep(2)

root = Tk()
root['bg'] = 'white'
root.title('Таблица умножения')
root.geometry('300x100')
root.lift()
root.attributes("-topmost", True)
root.resizable(width=False, height=False)

a = random.randrange(2,9)
b = random.randrange(2,9)
c = a*b
a1 = random.randrange(2,9)
b1 = random.randrange(2,9)
c1 = a1*b1
a2 = random.randrange(2,9)
b2 = random.randrange(2,9)
c2 = a2*b2

tata = '{0} x {1} = '.format(a,b)
tatat = '{0} x {1} = '.format(a1,b1)
tatata = '{0} x {1} = '.format(a2,b2)

lbl = Label(root, text=tata, font=('Arial Blod', 15), bg="white")
lbl.grid(column=0, row=0)
txt = Entry(root, width=10, font=('Arial Blod', 15))
txt.grid(column=1, row=0)

lbl1 = Label(root, text=tatat, font=('Arial Blod', 15), bg="white")
lbl1.grid(column=0, row=1)
txt1 = Entry(root, width=10, font=('Arial Blod', 15))
txt1.grid(column=1, row=1)

lbl2 = Label(root, text=tatata, font=('Arial Blod', 15), bg="white")
lbl2.grid(column=0, row=2)
txt2 = Entry(root, width=10, font=('Arial Blod', 15))
txt2.grid(column=1, row=2)

cls()
print('Привет Алена! Для того, чтоты сидеть за компьютером тебе нужно вспомнить таблицу умножения!')
print('Для проверки нужно нажать на черное окно и кнопку Enter')

prov = True
while prov:
    try:
        one = txt.get()
        two = txt1.get()
        free = txt2.get()
        one = int(one)
        two = int(two)
        free = int(free)
    except ValueError:
        ghj = 0
    if one == c:
        print('Первое правильно')
        if two == c1:
            print('Второе правильно')
            if free == c2:
                prov = True
                print('Третье правильно')
                os.system('C:\Windows\explorer.exe')
    root.update()
    dima = input()
    if dima == 'Dima':
        print('////Ответы////')
        print(c,c1,c2)
        print('////Ответы////')
    elif dima == 'Explorer':
        print('////Восстановление////')
        print('////Восстановление////')
        print('////Восстановление////')
        os.system('C:\Windows\explorer.exe')
exit()
