import tkinter as tk
import random
from pygame import mixer
import time


def close():
    window.destroy()


def key_part():
    code = []
    letters_list = 'abcdefghijklmnopqrstuvwxyz'
    for i in range(3):
        code += random.choice(letters_list)
    for i in range(2):
        code += str(random.randint(0, 10))
    random.shuffle(code)
    return code


def clicked():
    lbl_text.configure(text="Ваш ключ:")
    key1.grid(column=3, row=0)
    key2.grid(column=4, row=0)
    key3.grid(column=5, row=0)


window = tk.Tk()
window.geometry('800x600')
bg_img = tk.PhotoImage(file='tetr.png')

mixer.init()
mixer.music.load('8bit.mp3')
mixer.music.play(-1)

lbl = tk.Label(window, image=bg_img)
lbl.place(x=0, y=0, relwidth=1, relheight=1)

lbl_text = tk.Label(window, text="Добро пожаловать в мир тетриса", font=("Arial Bold", 20), bg='green', fg="white")
lbl_text.grid(column=2, row=0)

frame = tk.Frame(window, bg='orange')
frame.grid(column=0, row=0)

key1 = tk.Label(window, text=key_part(), font=("Arial Bold", 10), bg='black', fg="white")
key2 = tk.Label(window, text=key_part(), font=("Arial Bold", 10), bg='black', fg="white")
key3 = tk.Label(window, text=key_part(), font=("Arial Bold", 10), bg='black', fg="white")

btn = tk.Button(window, text="Сгенерировать ключ", command=clicked)
btn.grid(column=6, row=0)

btn_exit = tk.Button(frame, text='Cancel', command=close)
btn_exit.grid(column=2, row=3, padx=10, pady=15)

window.mainloop()