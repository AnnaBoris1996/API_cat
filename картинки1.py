from cProfile import label
from tkinter import *
import requests
from PIL import Image, ImageTk
from io import BytesIO

from bottle import response
from pygame.examples.aliens import load_image
from pygame.examples.cursors import image


def load_image():
    response=requests.get(url)
    image_data=BytesIO(response.content)
    img=Image.open(image_data)
    img.thumbnail((500,500))#подгоняем под размер
    img=ImageTk.PhotoImage(img)
    label.image = img
    label.config(image=img)


w=Tk()
w.geometry("550x550")

label=Label(width=500, height=500)
label.pack()

url="https://cataas.com/cat"

mainmenu=Menu(w)
w.config(menu=mainmenu)
file_menu=Menu(mainmenu, tearoff=0)
mainmenu.add_cascade(label="Файл", menu=file_menu)
file_menu.add_command(label="Загрузка изображения", command=load_image)
file_menu.add_command(label="Выход", command=w.destroy)

load_image()

w.mainloop()