from cProfile import label
from tkinter import *
import requests
from PIL import Image, ImageTk
from io import bytesIO

from bottle import response
from pygame.examples.aliens import load_image

def load_image(url):
    response=requests.get()
    print(response)

w=Tk()
w.geometry("500x500")

label=Label()
label.pack()

url="https://cataas.com/cat"
img=load_image(url)

if img:
    label.config(image=img)
    label.image=img

w.mainloop()