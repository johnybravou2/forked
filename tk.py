from tkinter import ttk
from tkinter import *
import requests
from PIL import ImageTk, Image
from tkcalendar import DateEntry


API_ENDPOINT1 = "http://127.0.0.1:8000/show_available_room"
ADD_TO_CART = "http://127.0.0.1:8000/add_to_cart"

Hotel = ["Kirimayaresort","Muthimaya","Atta"]

temp = []
start_page_list = []
root = Tk()
def on_click():
    global photo1
    global photo2

    photo1 = None
    photo2 = None
    st_date = cal.get_date()
    str_start=st_date.strftime("%d-%m-%Y")
    end_date = cal2.get_date()
    str_end=end_date.strftime("%d-%m-%Y")
    
    if (end_date-st_date).days >=1:
        
        for label in temp: 
            label.destroy()

        print(len(temp))
        #myWindow.title("room")
        #myWindow.geometry = ("1024x720+200+50")

        print('on click')

        
        payload = {
            "Hotel" : select_hotel.get(),
            "start_date": str_start,
            "end_date": str_end, 
        }
        response = requests.post(API_ENDPOINT1, json=payload)
        if response.ok:
            imgs = []
            value_list = []
            data = response.json()
            data = data['Data']
            keys = []
            i=0


            for key,value in data.items():
            
                value_list.append(value)
                keys.append(key)
                print(value)
                
                tmp = Button(root, text=str(key), bg="green", command=lambda: on_click2(keys[-1]))
                tmp.place(x=100,y=150+i)
                temp.append(tmp)
                #imgs.append(PhotoImage(file=value))
                i+=200
                #print(imgs)
                #tmp2 = Label(root, image= imgs[-1], width=60, height=80)
                #tmp2.place(x=300,y=200+i)

                #temp.append(tmp2)
           


            print(value_list)
            j=0
            k=0
            i=0
            
            for i,image_path in enumerate(value_list):
                img = Image.open(image_path)
                img = img.resize((150, 150), Image.ANTIALIAS)
                img = ImageTk.PhotoImage(img)
                imgs.append(img)
                label = Label(root, image=img)
                label.place(x=300 if i % 2 == 0 else 400, y=500 + (i // 2) * 200)
                temp.append(label)


            print(len(temp))
            #j=0
            #if len(value_list) == 1:
            #    photo1 = PhotoImage(file=value_list[0])
            #    label1 = Label(myWindow,image=photo1).place(x=300,y=100)
            #
            #if len(value_list) == 2:
            #    print('kuy')
            #    photo1 = PhotoImage(file=value_list[0])
            #    photo2 = PhotoImage(file=value_list[1])
            #    print(photo1)
            #    print(photo2)
            #    label1 = Label(myWindow,image=photo1).place(x=300,y=100)
            #    
            #    j+=150
            #    label2 = Label(myWindow,image=photo2).place(x=300,y=100+j)
            #myWindow.mainloop()
    else:
        print("rai wa")
        e = Label(root, text= '"No reserved room"',fg=("red"))
        e.place(x=490,y=5)
        temp.append(e)

def on_click2(room):
    print("on click2")
    st_date = cal.get_date()
    end_date = cal2.get_date()
    print(room)
    payload = {
            "Room" : room,
            "Night": str(end_date-st_date)
         }
    response = requests.post(ADD_TO_CART, json=payload)
    if response:
        data = response.json()
        data = data['Data']
       
            

        tmp = Label(root, text='add to cart success')
        tmp.place(x=700,y=600)
        temp.append(tmp)

root.title("Kiri")
dayin = StringVar()
monthin  = StringVar()
yearin = StringVar()
dayout = StringVar()
monthout  = StringVar()
yearout = StringVar()
select_hotel = StringVar()
sel_start =StringVar()
sel_end =StringVar()
#def start_page():
 # declaring string variable 

class RoomDetailsPage(Frame):
    def __init__(self, parent, room):
        Frame.__init__(self, parent)

        # โหลดรูปภาพห้องพัก
        room_image = Image.open(room.image_path)
        room_image = room_image.resize((400, 300), Image.ANTIALIAS)
        room_photo = ImageTk.PhotoImage(room_image)

        # แสดงรูปภาพห้องพัก
        image_label = Label(self, image=room_photo)
        image_label.image = room_photo
        image_label.pack()

        # แสดงชื่อห้องพัก
        name_label = Label(self, text=f"ชื่อห้องพัก: {room.name}")
        name_label.pack()

        # แสดงรายละเอียดของห้องพัก
        description_label = Label(self, text=room.description)
        description_label.pack()

        # แสดงราคาห้องพัก
        price_label = Label(self, text=f"ราคา: {room.price} บาท/คืน")
        price_label.pack()

        # แสดงปุ่มปิดหน้าต่าง
        close_button = ttk.Button(self, text="ปิด", command=self.destroy)
        close_button.pack()

def start_page():
    global cal
    global cal2

    cal=DateEntry(root,selectmode='day',textvariable=sel_start)
    cal.place(x=200,y=30)
    start_page_list.append(cal)

    cal2=DateEntry(root,selectmode='day',textvariable=sel_end)
    cal2.place(x=470,y=30)
    start_page_list.append(cal2)

    btn = Button(root, text="Search", bg="green", command=on_click)
    btn.place(x = 485, y = 80)
    start_page_list.append(btn)

    choose_hotel = OptionMenu(root, select_hotel, *Hotel)
    choose_hotel.config(width=15)
    choose_hotel.place(x= 650,y = 27)
    start_page_list.append(choose_hotel)



start_page()

root.geometry("1024x720+200+50")

root.mainloop()


