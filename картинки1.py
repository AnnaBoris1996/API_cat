from cProfile import label
from tkinter import *
import requests
from PIL import Image, ImageTk
from io import BytesIO

from bottle import response
from pygame.examples.aliens import load_image
from pygame.examples.cursors import image


def load_image(url):
    response=requests.get(url)
    print(response)
    image_data=BytesIO(response.content)
    print(response.headers)
    img=Image.open(image_data)
    print(img)
    return ImageTk.PhotoImage(img)

w=Tk()
w.geometry("500x500")

label=Label()
label.pack()

url="https://cataas.com/cat"
img=load_image(url)

if img:
    label.config(image=img)
    label.image=img

but=Button(text="Обновить картинку", command=load_image)
but.pack()

w.mainloop()