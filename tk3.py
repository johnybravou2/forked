
from tkinter import *
import customtkinter as ctk
import requests
from PIL import ImageTk, Image
from tkcalendar import DateEntry
from functools import partial
temp = []

class StartPage(ctk.CTk):
    def __init__(self, parent, controller):
        super().__init__()
        Frame.__init__(self,parent)
        self.hotel = ["Kirimayaresort","Muthimaya","Atta"]
        self.cal=DateEntry(parent,selectmode='day')
        self.cal.place(x=200,y=30)
        self.cal2=DateEntry(parent,selectmode='day')
        self.cal2.place(x=470,y=30)
        self.btn = Button(parent, text="Search", bg="green", command=lambda: self.search_rooms(parent, controller))
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
    def search_rooms(self, parent, controller):
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
                keys = []
                for room in data:
                    img = PhotoImage(file=f"{room['_room_pic']}")
                    imgs.append(img)
                    label_img = Button(self, image=img, command=partial(controller.change_frame, BookingPage))
                    label_img.place(x=400,y=200+i)
                    text = f"{room['_room_name']}"
                    btn = Button(self, text=f"{room['_room_name']}", command=partial(self.show_room, room, controller))
                    btn.place(x=200,y=200+i)
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

    

    def show_room(self,room, controller):
        print(room)
        #controller.change_frame()
        self.root = Toplevel()
        self.root.geometry("360x200+280+280")
        
        button=Button(self.root, text="Back", bg="green", command= lambda: self.parent.destroy())
        #img = Image.open(f"{room['_room_pic']}")
        #img = img.resize((400, 400))
        #img = PhotoImage(img)
        
        #lab2= Label(self.parent, image=img)
        #lab2.place(x=10, y=10)
        lab1= Label(self.root, text=f"{room['_room_name']}", font=25 )
        lab1.place(x=100,y=20)
        lab2= Label(self.root, text="Room Space: "+ f"{room['_room_area']}",font=20)
        lab2.place(x=65,y=50)
        lab3= Label(self.root, text="Number of Bedrooms: "+ f"{room['_number_of_bedroom']}",font=20)
        lab3.place(x=40,y=80)
        lab4= Label(self.root, text="Number of Bathrooms: "+ f"{room['_number_of_bathroom']}",font=20)
        lab4.place(x=30,y=110)
        
        
        button.place(x=10,y=10)
        self.root.mainloop()


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


class BookingPage(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self,parent)
        self.titles = ['Mr.','Ms.','Mrs.','Dr.','Others']
        self.countries = ['Afghanistan', 'Albania', 'Algeria', 'Andorra', 'Angola', 'Antigua and Barbuda', 'Argentina', 'Armenia', 'Australia', 'Austria', 'Azerbaijan', 'Bahamas', 'Bahrain', 'Bangladesh', 'Barbados', 'Belarus', 'Belgium', 'Belize', 'Benin', 'Bhutan', 'Bolivia', 'Bosnia and Herzegovina', 'Botswana', 'Brazil', 'Brunei', 'Bulgaria', 'Burkina Faso', 'Burundi', 'Cabo Verde', 'Cambodia', 'Cameroon', 'Canada', 'Central African Republic (CAR)', 'Chad', 'Chile', 'China', 'Colombia', 'Comoros', 'Congo, Democratic Republic of the', 'Congo, Republic of the', 'Costa Rica', "Cote d'Ivoire", 'Croatia', 'Cuba', 'Cyprus', 'Czech Republic (Czechia)', 'Denmark', 'Djibouti', 'Dominica', 'Dominican Republic', 'Ecuador', 'Egypt', 'El Salvador', 'Equatorial Guinea', 'Eritrea', 'Estonia', 'Eswatini (formerly Swaziland)', 'Ethiopia', 'Fiji', 'Finland', 'France', 'Gabon', 'Gambia', 'Georgia', 'Germany', 'Ghana', 'Greece', 'Grenada', 'Guatemala', 'Guinea', 'Guinea-Bissau', 'Guyana', 'Haiti', 'Honduras', 'Hungary', 'Iceland', 'India', 'Indonesia', 'Iran', 'Iraq', 'Ireland', 'Israel', 'Italy', 'Jamaica', 'Japan', 'Jordan', 'Kazakhstan', 'Kenya', 'Kiribati', 'Kosovo', 'Kuwait', 'Kyrgyzstan', 'Laos', 'Latvia', 'Lebanon', 'Lesotho', 'Liberia', 'Libya', 'Liechtenstein', 'Lithuania', 'Luxembourg', 'Madagascar', 'Malawi', 'Malaysia', 'Maldives', 'Mali', 'Malta', 'Marshall Islands', 'Mauritania', 'Mauritius', 'Mexico', 'Micronesia', 'Moldova', 'Monaco', 'Mongolia', 'Montenegro', 'Morocco', 'Mozambique', 'Myanmar (formerly Burma)', 'Namibia', 'Nauru', 'Nepal', 'Netherlands', 'New Zealand', 'Nicaragua', 'Niger', 'Nigeria', 'North Korea', 'North Macedonia (formerly Macedonia)', 'Norway', 'Oman', 'Pakistan', 'Palau', 'Palestine', 'Panama', 'Papua New Guinea', 'Paraguay', 'Peru', 'Philippines', 'Poland', 'Portugal', 'Qatar', 'Romania', 'Russia', 'Rwanda', 'Saint Kitts and Nevis', 'Saint Lucia', 'Saint Vincent and the Grenadines', 'Samoa', 'San Marino', 'Sao Tome and Principe', 'Saudi Arabia', 'Senegal', 'Serbia', 'Seychelles', 'Sierra Leone', 'Singapore', 'Slovakia', 'Slovenia', 'Solomon Islands', 'Somalia', 'South Africa', 'South Korea', 'South Sudan', 'Spain', 'Sri Lanka', 'Sudan', 'Suriname', 'Sweden', 'Switzerland', 'Syria', 'Taiwan', 'Tajikistan', 'Tanzania', 'Thailand', 'Timor-Leste (formerly East Timor)', 'Togo', 'Tonga', 'Trinidad and Tobago', 'Tunisia', 'Turkey', 'Turkmenistan', 'Tuvalu', 'Uganda', 'Ukraine', 'United Arab Emirates (UAE)', 'United Kingdom (UK)', 'United States of America (USA)', 'Uruguay', 'Uzbekistan', 'Vanuatu', 'Vatican City (Holy See)', 'Venezuela', 'Vietnam', 'Yemen', 'Zambia', 'Zimbabwe']
        self.name = StringVar()
        self.surname = StringVar()
        self.email = StringVar()
        self.address = StringVar()
        self.nationality = StringVar()
        self.phonenumber = StringVar()
        self.gname = StringVar()
        self.emailcontact = StringVar()



        self.lab1= Label(parent, text="Title:")
        self.lab1.place(x=10,y=20)
        
        self.title = StringVar()
        self.titleom = OptionMenu(parent, self.title, *self.titles)
        self.titleom.config(width=5,justify=LEFT)
        self.titleom.place(x=10,y=40)
        
        
        Label(parent, text="First Name:").place(x=80, y=20, width=90, height=25)
        entryname = Entry(parent,textvariable=self.name,width=20,justify=LEFT).place(x=95, y=50, width=100, height=35)
        Label(parent, text="Last Name:").place(x=180, y=20, width=90, height=25)
        entrysurname = Entry(parent,textvariable=self.surname,width=20,justify=LEFT).place(x=205, y=50, width=100, height=35)
        Label(parent, text="Email address:").place(x=10, y=80, width=90, height=25)
        emailentry = Entry(parent,textvariable=self.email,width=50,justify=LEFT).place(x=10, y=110, width=260, height=25)
        Label(parent, text="Address:").place(x=10, y=140, width=60, height=25)
        Entry(parent,textvariable=self.address,width=60,justify=LEFT).place(x=10, y=170, width=260, height=25)
        Label(parent, text="Nationality:").place(x=10, y=200, width=80, height=25)
        countryom = OptionMenu(parent,self.nationality,*self.countries)
        countryom.config(width=25,justify=LEFT)
        countryom.place(x=10, y=230, width=260, height=25)
        Entry(parent,textvariable=self.phonenumber,width=15,justify=LEFT).place(x=280, y=230, width=90, height=25)
        Label(parent, text="Room Details").place(x=10, y=270, width=80, height=25)
        Label(parent, text="Guest Name:").place(x=10, y=300, width=80, height=25)
        gentry = Entry(parent,textvariable=self.gname,width=20,justify=LEFT).place(x=10, y=330, width=90, height=25)
        Label(parent, text="E-mail for individual room confirmation:").place(x=110, y=300, width=220, height=25)
        emailcontactentry = Entry(parent,textvariable=self.emailcontact,width=50,justify=LEFT).place(x=110, y=330, width=220, height=25)
        Label(parent, text="Other Requirement(s):").place()




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



if __name__ == "__main__":
    app = MainApp()
    app.geometry("1024x700")
    app.mainloop()