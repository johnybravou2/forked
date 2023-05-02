from tkinter import ttk
from tkinter import *
import requests
from PIL import ImageTk, Image
from tkcalendar import DateEntry
temp = []

class StartPage(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self,parent)
        self.hotel = ["Kirimayaresort","Muthimaya","Atta"]
        self.cal=DateEntry(parent,selectmode='day')
        self.cal.place(x=200,y=30)
        self.cal2=DateEntry(parent,selectmode='day')
        self.cal2.place(x=470,y=30)
        self.btn = Button(parent, text="Search", bg="green", command=lambda: self.search_rooms())
        self.btn.place(x = 485, y = 80)

        self.selected_hotel = StringVar()
        self.choose_hotel = OptionMenu(parent, self.selected_hotel, *self.hotel)
        self.choose_hotel.config(width=15)
        self.choose_hotel.place(x= 650,y = 27)

    
        

      
#
        #self.lbl_check_in = Label(master, text="Check-in date:")
        #self.lbl_check_in.grid(row=0, column=0)
#
        #self.ent_check_in = Entry(master)
        #self.ent_check_in.grid(row=0, column=1)
#
        #self.lbl_check_out = Label(master, text="Check-out date:")
        #self.lbl_check_out.grid(row=1, column=0)
#
        #self.ent_check_out = Entry(master)
        #self.ent_check_out.grid(row=1, column=1)
#
        #self.lbl_hotel = Label(master, text="Select hotel:")
        #self.lbl_hotel.grid(row=2, column=0)
#
        #self.opt_hotel = tk.OptionMenu(master, tk.StringVar(), "Hotel A", "Hotel B", "Hotel C")
        #self.opt_hotel.grid(row=2, column=1)
#
        #self.btn_search = tk.Button(master, text="Search", command=self.search_rooms)
        #self.btn_search.grid(row=3, column=0)
#
        #self.frame_rooms = tk.Frame(master)
        #self.frame_rooms.grid(row=4, column=0, columnspan=2)
#
    def search_rooms(self):
        API_ENDPOINT1 = "http://127.0.0.1:8000/show_available_room"
        if (self.cal2.get_date()-self.cal.get_date()).days >=1:
            
            payload = {
                "Hotel" : str(self.selected_hotel.get()),
                "start_date": self.cal.get_date().strftime("%d-%m-%Y"),
                "end_date": self.cal2.get_date().strftime("%d-%m-%Y")
            }
            print(str(self.selected_hotel.get()))
            response = requests.post(API_ENDPOINT1, json=payload)
            if response.ok:
                imgs = []
                
                for label in temp:
                    label.destroy()
                data = response.json()
                data = data['Data']
                print(data)
                i=0
                j=1
                for room in data:
                    img = PhotoImage(file=f"{room['_room_pic']}")
                    imgs.append(img)
                    label_img = Label(self, image=img )
                    label_img.place(x=400,y=240+i)
                    text = f"{room['_room_name']}"
                    btn = Button(self, text=text, command=lambda j=j: self.show_room(text))
                    btn.place(x=200,y=240+i)
                    temp.append(btn)
                    j+=1
                    i+=150


            if response.status_code == 200:
                self.show_rooms(response.json())
        else:
            print("rai wa")
            e = Label(self, text= '"No reserved room"',fg=("red"))
            e.place(x=490,y=5)
            temp.append(e)


    def show_room(self,room):
        print(room)



    def show_rooms(self, rooms):
        self.frame_rooms.destroy()
        self.frame_rooms = Frame(self.master)
        self.frame_rooms.grid(row=4, column=0, columnspan=2)

        for room in rooms:
            frame_room = Frame(self.frame_rooms, pady=10)
            frame_room.pack()

            img_room = PhotoImage(file=f"{room['image']}")
            lbl_img = Label(frame_room, image=img_room)
            lbl_img.pack(side=LEFT)

            lbl_name = Label(frame_room, text=f"{room['name']}")
            lbl_name.pack(side=LEFT)

            lbl_description = Label(frame_room, text=f"{room['description']}")
            lbl_description.pack(side=LEFT)

            lbl_price = Label(frame_room, text=f"{room['price']}")
            lbl_price.pack(side=LEFT)

            btn_book = Button(frame_room, text="Book", command=lambda room_id=room['id']: self.book_room(room_id))
            btn_book.pack(side=LEFT)

    def book_room(self, room_id):
        url = f"http://127.0.0.1:8000/add_to_cart"
        data = {"room_id": room_id}
        response = requests.post(url, json=data)

        if response.status_code == 200:
            message = "Room has been added to cart!"
        else:
            message = "Failed to add room to cart."

        messgebox.showinfo("Booking Result", message)


class MainApp(Tk):
    def __init__(self):
        Tk.__init__(self) 
        self.container = Frame(self)
        self.container.pack(fill=BOTH,expand=YES)
        self.container.config()
        
        self.frame = StartPage(self.container,self)
        self.frame.pack(fill=BOTH,expand=YES)

    def change_frame(self,frame):
        self.frame.destroy()
        self.frame = frame(self.container,self)
        self.frame.pack(fill=BOTH,expand=YES)

app = MainApp()
app.geometry("1280x720")
app.mainloop()