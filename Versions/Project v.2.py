import os
import random
from time import sleep
from tkinter import *

def numbers():
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
    lbl.configure(text=(tata))
    lbl1.configure(text=(tatat))
    lbl2.configure(text=(tatata))
    return c,c1,c2

os.system("taskkill/IM explorer.exe /F")
os.system('CLS')
sleep(2)

root = Tk()
root['bg'] = 'white'
root.title('Примеры')
root.geometry('250x100')
root.lift()
root.attributes("-topmost", True)
root.resizable(width=False, height=False)

lbl = Label(root, text='Загрузка...', font=('Arial Blod', 15), bg="white")
lbl.grid(column=0, row=0)
txt = Entry(root, width=10, font=('Arial Blod', 15))
txt.grid(column=1, row=0)
lbl1 = Label(root, text='Загрузка...', font=('Arial Blod', 15), bg="white")
lbl1.grid(column=0, row=1)
txt1 = Entry(root, width=10, font=('Arial Blod', 15))
txt1.grid(column=1, row=1)
lbl2 = Label(root, text='Загрузка...', font=('Arial Blod', 15), bg="white")
lbl2.grid(column=0, row=2)
txt2 = Entry(root, width=10, font=('Arial Blod', 15))
txt2.grid(column=1, row=2)

c,c1,c2 = numbers()
print('Привет Алена! Для того, чтоты сидеть за компьютером тебе нужно вспомнить таблицу умножения!\nДля проверки нужно нажать на черное окно и кнопку Enter')

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
        poxuy = True
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
        print('\n////Ответы////' * 2)
        print(c,c1,c2)
        print('////Ответы////\n' * 2)
    elif dima == 'Explorer':
        print('\n////Восстановление////' * 3)
        os.system('C:\Windows\explorer.exe')
exit()
