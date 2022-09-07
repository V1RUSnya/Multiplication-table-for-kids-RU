import os
import random
from time import sleep
from tkinter import *

def one(c):
    b = False
    try:
        a = txt.get()
        a = int(a)
        if a == c:
            b = True
            print('Первый пример решен верно!')
        else:
            b = False
    except:
        c = ''
    return b

def two(c):
    b = False
    try:
        a = txt1.get()
        a = int(a)
        if a == c:
            b = True
            print('Второй пример решен верно!')
        else:
            b = False
    except:
        c = ''
    return b

def free(c):
    b = False
    try:
        a = txt2.get()
        a = int(a)
        if a == c:
            b = True
            print('Третий пример решен верно!')
        else:
            b = False
    except:
        c = ''
    return b

def numbers():
    a = random.randrange(3,9)
    b = random.randrange(3,9)
    c = a*b
    a1 = random.randrange(3,9)
    b1 = random.randrange(3,9)
    c1 = a1*b1
    a2 = random.randrange(3,9)
    b2 = random.randrange(3,9)
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
prov = True

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

print('Привет Алена! Для того, чтобы сидеть за компьютером тебе нужно вспомнить таблицу умножения!\nЗагрузка...')
root.update()
sleep(10)
c,c1,c2 = numbers()
c,c1,c2 = int(c),int(c1),int(c2)

while prov:
    abc = one(c)
    abc1 = two(c1)
    abc2 = free(c2)
    print('------------------------------')
    if abc == True and abc1 == True and abc2 == True:
        print('Все решено, молодец!')
        os.system('C:\Windows\explorer.exe')
        prov = False
    dima = txt.get()
    if dima == 'Dima' or dima == 'Дима':
        print(c,c1,c2)
    elif dima == 'Explorer' or dima == 'Эксплорер' or dima == '2911':
        print('\n////Восстановление////' * 3)
        os.system('C:\Windows\explorer.exe')
        prov = False
    root.update()
    sleep(0.1)
root.mainloop()
