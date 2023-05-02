from tkinter import *
from PIL import ImageTk, Image
from tkcalendar import *

root =Tk()

value_list = ["PICTURE\\PLANTATION.png","PICTURE\\HORIZON.png"]
cal = Calendar(root, selectmode="day",year=2023, month=5, day=2)
cal.place(x=0,y=0)
my_label = Label()

def grab_date():
    my_label.config(text=cal.get_date())
    
imgs = []
k=0
j=0
for i in range(len(value_list)):
    imgs.append(ImageTk.PhotoImage(file=value_list[j]))
    print(j)
    Label(root, image=imgs[-1], width=60, height=80).place(x=300,y=200+k)
    j+=1
    k+=200


search = Button(root, text=("search"), command=grab_date())
search.place(x=250,y=50)

my_label = Label(root,text="")
my_label.place(x=100,y=200)





root.mainloop()