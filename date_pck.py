from tkinter import ttk
from tkinter import *
import requests
from PIL import ImageTk, Image
from tkcalendar import DateEntry
imgs=[]
temp=[]
value_list = ['PICTURE\\PLANTATION.png', 'PICTURE\\HORIZON.png']

root = Tk()

i=0
for i,image_path in enumerate(value_list):
    img = Image.open(image_path)
    img = img.resize((150, 150), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(img)
    imgs.append(img)
    label = Label(root, image=img)
    label.place(x=200 if i % 2 == 0 else 400, y=200 + (i // 2) * 200)
    temp.append(label)

root.mainloop()