from tkinter import ttk
from tkinter import *
import requests
import customtkinter as ctk
from PIL import ImageTk, Image
from tkcalendar import DateEntry
from tkcalendar import Calendar
from functools import partial
import re
from datetime import datetime
import json
import main as r


class SearchPage():
    def __init__(self):
        global date_in
        global date_out
        global selected_room

        self.temp=[]
        self.__root = ctk.CTk()
        self.__root.title("Kirimaya")
        self.__root.geometry("870x720")
        self.__root.minsize(870 ,600)
        self.hotel = ["Kirimayaresort","Muthimaya","Atta"]
        self.cal=DateEntry(self.__root,selectmode='day')
        self.cal.place(x=240,y=50)
        self.cal2=DateEntry(self.__root,selectmode='day')
        self.cal2.place(x=470,y=50)
        self.btn = Button(self.__root, text="Search", bg="green", command= lambda:self.search_rooms())
        self.btn.place(x = 500, y = 100)
        self.selected_hotel = StringVar()
        
        self.choose_hotel = OptionMenu(self.__root, self.selected_hotel, *self.hotel)
        self.choose_hotel.config(width=15)
        self.choose_hotel.place(x= 660,y = 45)
        button=Button(self.__root, text="Back", bg="green", command= lambda: self.back())
        button.place(x=10,y=10)
        
        selected_room = None
        self.__root.mainloop()
        

    def back(self):
        self.__root.destroy()
        MainApp()  
    

    def search_rooms(self):
        API_ENDPOINT1 = "http://127.0.0.1:8000/show_available_room"
        global date_in
        global date_out

        date_in = self.cal.get_date()
        date_out = self.cal2.get_date()

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
                night = (self.cal2.get_date()-self.cal.get_date()).days
                for label in self.temp:
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
                    label_img = Label(self.__root, image=img )
                    label_img.place(x=430,y=200+i)
                    price = str(int(f"{room['_room_price']}") * night)
                    lab_name = Label(self.__root, text=f"{room['_room_name']}", font=23)
                    lab_name.place(x=115,y=200+i)
                    btn = Button(self.__root, text="View details", command=partial(self.show_room, room))
                    btn2 = Button(self.__root, text="Book this room",  command=partial(self.go_to_book, room,))
                    price_lab = Label(self.__root, text=price + "  THB",font=25)
                    price_lab.place(x=700, y=200+i)
                    btn.place(x=125,y=250+i)
                    btn2.place(x=700,y=240+i)
                    self.temp.append(btn)
                    self.temp.append(btn2)
                    self.temp.append(price_lab)
                    self.temp.append(lab_name)
                    j+=1
                    i+=180
          


            if response.status_code == 200:
                self.show_rooms(response.json())

        else:
            print("rai wa")
            e = Label(self.__root, text= '"No reserved room"',fg=("red"))
            e.place(x=490,y=5)
            self.temp.append(e)


       

    

    def show_room(self,room):
        print(room)
        
        self.root = Toplevel()
        self.root.title("Detail")
        self.root.geometry("420x200+280+280")
        
        button=Button(self.root, text="Back", bg="green", command= lambda: self.root.destroy())
        
        lab1= Label(self.root, text=f"{room['_room_name']}", font=25 )
        lab1.place(x=70,y=20)
        lab2= Label(self.root, text="Room Space: "+ f"{room['_room_area']}",font=20)
        lab2.place(x=70,y=50)
        lab3= Label(self.root, text="Number of Bedrooms: "+ f"{room['_number_of_bedroom']}",font=20)
        lab3.place(x=70,y=80)
        lab4= Label(self.root, text="Number of Bathrooms: "+ f"{room['_number_of_bathroom']}",font=20)
        lab4.place(x=70,y=110)
        lab5=  Label(self.root, text=f"{room['_room_price']}"+"  THB per night",font=20)
        lab5.place(x=70,y=140)
        
        button.place(x=10,y=10)
        self.root.mainloop()


    def go_to_book(self, room):
        self.__root.destroy()
        BookingPage(room)



class BookingPage():
    API_ENDPOINT2 = "http://127.0.0.1:8000/book_room"

    def __init__(self, room):
        self.selected_room = room

        self.titles = ['Mr.','Ms.','Mrs.','Dr.','Others']
        self.countries = ['Afghanistan', 'Albania', 'Algeria', 'Andorra', 'Angola', 'Antigua and Barbuda', 'Argentina', 'Armenia', 'Australia', 'Austria', 'Azerbaijan', 'Bahamas', 'Bahrain', 'Bangladesh', 'Barbados', 'Belarus', 'Belgium', 'Belize', 'Benin', 'Bhutan', 'Bolivia', 'Bosnia and Herzegovina', 'Botswana', 'Brazil', 'Brunei', 'Bulgaria', 'Burkina Faso', 'Burundi', 'Cabo Verde', 'Cambodia', 'Cameroon', 'Canada', 'Central African Republic (CAR)', 'Chad', 'Chile', 'China', 'Colombia', 'Comoros', 'Congo, Democratic Republic of the', 'Congo, Republic of the', 'Costa Rica', "Cote d'Ivoire", 'Croatia', 'Cuba', 'Cyprus', 'Czech Republic (Czechia)', 'Denmark', 'Djibouti', 'Dominica', 'Dominican Republic', 'Ecuador', 'Egypt', 'El Salvador', 'Equatorial Guinea', 'Eritrea', 'Estonia', 'Eswatini (formerly Swaziland)', 'Ethiopia', 'Fiji', 'Finland', 'France', 'Gabon', 'Gambia', 'Georgia', 'Germany', 'Ghana', 'Greece', 'Grenada', 'Guatemala', 'Guinea', 'Guinea-Bissau', 'Guyana', 'Haiti', 'Honduras', 'Hungary', 'Iceland', 'India', 'Indonesia', 'Iran', 'Iraq', 'Ireland', 'Israel', 'Italy', 'Jamaica', 'Japan', 'Jordan', 'Kazakhstan', 'Kenya', 'Kiribati', 'Kosovo', 'Kuwait', 'Kyrgyzstan', 'Laos', 'Latvia', 'Lebanon', 'Lesotho', 'Liberia', 'Libya', 'Liechtenstein', 'Lithuania', 'Luxembourg', 'Madagascar', 'Malawi', 'Malaysia', 'Maldives', 'Mali', 'Malta', 'Marshall Islands', 'Mauritania', 'Mauritius', 'Mexico', 'Micronesia', 'Moldova', 'Monaco', 'Mongolia', 'Montenegro', 'Morocco', 'Mozambique', 'Myanmar (formerly Burma)', 'Namibia', 'Nauru', 'Nepal', 'Netherlands', 'New Zealand', 'Nicaragua', 'Niger', 'Nigeria', 'North Korea', 'North Macedonia (formerly Macedonia)', 'Norway', 'Oman', 'Pakistan', 'Palau', 'Palestine', 'Panama', 'Papua New Guinea', 'Paraguay', 'Peru', 'Philippines', 'Poland', 'Portugal', 'Qatar', 'Romania', 'Russia', 'Rwanda', 'Saint Kitts and Nevis', 'Saint Lucia', 'Saint Vincent and the Grenadines', 'Samoa', 'San Marino', 'Sao Tome and Principe', 'Saudi Arabia', 'Senegal', 'Serbia', 'Seychelles', 'Sierra Leone', 'Singapore', 'Slovakia', 'Slovenia', 'Solomon Islands', 'Somalia', 'South Africa', 'South Korea', 'South Sudan', 'Spain', 'Sri Lanka', 'Sudan', 'Suriname', 'Sweden', 'Switzerland', 'Syria', 'Taiwan', 'Tajikistan', 'Tanzania', 'Thailand', 'Timor-Leste (formerly East Timor)', 'Togo', 'Tonga', 'Trinidad and Tobago', 'Tunisia', 'Turkey', 'Turkmenistan', 'Tuvalu', 'Uganda', 'Ukraine', 'United Arab Emirates (UAE)', 'United Kingdom (UK)', 'United States of America (USA)', 'Uruguay', 'Uzbekistan', 'Vanuatu', 'Vatican City (Holy See)', 'Venezuela', 'Vietnam', 'Yemen', 'Zambia', 'Zimbabwe']
        self.__root = ctk.CTk()
        self.__root.title("Booking")
        self.__root.geometry("1024x720")
        self.__root.minsize(1000 ,600)
        self.name = StringVar()
        self.surname = StringVar()
        self.email = StringVar()
        self.phonenumber = StringVar()
        self.address = StringVar()
        self.nationality = StringVar()
        self.gname = StringVar()
        self.emailcontact = StringVar()
        self.card_number = StringVar()
        self.cvv = StringVar()
        self.night = (date_out-date_in).days
        self.temp =[]
        month_list= ['01','02','03','04','05','06','07','08','09','10','11','12']

        self.lab1 = Label(self.__root, text="Title:")
        self.lab1.place(x=90, y=70)

        self.title = StringVar()
        self.titleom = OptionMenu(self.__root, self.title, *self.titles)
        self.titleom.config(width=5, justify=LEFT)
        self.titleom.place(x=90, y=90)

        print(selected_room)
        
        Label(self.__root, text="First Name:").place(x=180, y=70, width=100, height=25)
        self.entryname = Entry(self.__root, textvariable=self.name, width=20, justify=LEFT).place(x=185, y=100, width=100, height=35)
        Label(self.__root, text="Last Name:").place(x=315, y=70, width=90, height=25)
        self.entrysurname = Entry(self.__root, textvariable=self.surname, width=20, justify=LEFT).place(x=320, y=100, width=100, height=35)
        Label(self.__root, text="Email :").place(x=70, y=140, width=90, height=25)
        self.entryemail = Entry(self.__root, textvariable=self.email, width=50, justify=LEFT).place(x=90, y=170, width=260, height=35)
        Label(self.__root, text="Address:").place(x=90, y=210, width=60, height=25)
        Entry(self.__root, textvariable=self.address, width=60, justify=LEFT).place(x=90, y=240, width=260, height=35)
        Label(self.__root, text="Nationality:").place(x=90, y=280, width=80, height=25)
        countryom = OptionMenu(self.__root, self.nationality, *self.countries)
        countryom.config(width=25, justify=LEFT)
        countryom.place(x=90, y=310, width=260, height=35)
        Label(self.__root, text="Phone number:").place(x=410, y=270, width=110, height=25)
        self.entryphone_number = Entry(self.__root, textvariable=self.phonenumber, width=15, justify=LEFT).place(x=410, y=300, width=90, height=35)
        

        Label(self.__root, text="Card number:").place(x=90, y=500)
        Entry(self.__root, textvariable=self.card_number, width=60, justify=LEFT).place(x=90, y=530, width=260, height=35)
        Label(self.__root, text="Expired date:").place(x=400, y=500)
        self.com1 = ttk.Combobox(self.__root, value= month_list, width = 5, height=8)
        self.com1.place(x=400, y=530)
        self.com2 = ttk.Combobox(self.__root, value= list(range(23,48)), width = 5, height=8)
        self.com2.place(x=470, y=530)
        Label(self.__root, text="CVV:").place(x=90, y=580)
        Entry(self.__root, textvariable=self.cvv, width=60, justify=LEFT).place(x=90, y=610, width=50, height=35)
        

        button=Button(self.__root, text="Back", bg="green", command= lambda: self.back())
        button.place(x=10,y=10)
       

        Label(self.__root, text=f"{self.selected_room['_room_name']}",font=35).place(x=750, y=50)
        
        lab2= Label(self.__root, text="Room Space: "+ f"{self.selected_room['_room_area']}",font=20)
        lab2.place(x=750,y=80)
        lab3= Label(self.__root, text="Number of Bedrooms: "+ f"{self.selected_room['_number_of_bedroom']}",font=20)
        lab3.place(x=750,y=110)
        lab4= Label(self.__root, text="Number of Bathrooms: "+ f"{self.selected_room['_number_of_bathroom']}",font=20)
        lab4.place(x=750,y=140)
        img = PhotoImage(file=f"{self.selected_room['_room_pic']}")
        lab5=Label(self.__root, image= img)
        lab5.place(x=750,y=220)
        lab6= Label(self.__root, text= str(self.night) +" x Night "  + str(int(f"{self.selected_room['_room_price']}")* self.night),font=20)
        lab6.place(x=750, y=170)
        Button(self.__root, text="Confirm",bg="green",font=30, command=partial(self.book_room)).place(x=600,y=600)
        
        self.__root.mainloop()

    
    def back(self):
        self.__root.destroy()
        SearchPage()

    def book_room(self):
        card_date = str(self.com1.get())+"/"+str(self.com2.get())
        print(card_date)
        

        for label in self.temp:
            label.destroy()

        if self.title.get() == ' ' or self.name.get() == ' 'or self.surname.get() == ''or self.email.get() == ''or self.phonenumber.get()== '':
            error = Label(self.__root, text="Please enter valid input", fg=("red"))
            error.place(x=600, y=570)
            self.temp.append(error)

        elif not self.is_valid_phone_number(self.phonenumber.get()):
            error = Label(self.__root, text="Not valid phone number", fg=("red"))
            error.place(x=600, y=570)
            self.temp.append(error)
        elif not self.is_valid_email(self.email.get()):
            error = Label(self.__root, text="Not valid email", fg=("red"))
            error.place(x=600, y=570)
            self.temp.append(error)  
        elif not self.is_valid_credit_card(self.card_number.get()):
            print("mic")
            error = Label(self.__root, text="Not valid card", fg=("red"))
            error.place(x=600, y=570)
            self.temp.append(error)  
        
        elif not self.is_valid_CVV(self.cvv.get()):
            error = Label(self.__root, text="Not valid cvv", fg=("red"))
            error.place(x=600, y=570)
            self.temp.append(error)
        
               
        elif self.is_credit_card_expired(card_date):
            error = Label(self.__root, text="Credit card expired", fg=("red"))
            error.place(x=600, y=570)
            self.temp.append(error)
       
        
        
        else:    
            API_ENDPOINT2 = "http://127.0.0.1:8000/book_room"
            payload = {
                    "room" : f"{self.selected_room['_room_name']}",
                    "start_date": date_in.strftime("%d-%m-%Y"),
                    "end_date": date_out.strftime("%d-%m-%Y"),
                    "title": self.title.get(),
                    "name": self.name.get(),
                    "surname":self.surname.get(),
                    "email":self.email.get(),
                    "phone_number":self.phonenumber.get()
                }
            print(payload)
            response = requests.post(API_ENDPOINT2, json=payload)
            if response.ok:
                print("wow")
                data = response.json()
                data = data['Data']
                self.__root.destroy()
                SuccessPage(data)
                print(data)

    def is_valid_email(self,email):
    
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

    
        if re.search(pattern, email):
            return True
        else:
            return False
        
    def is_valid_credit_card(self,number):
        
        number = number.replace(' ', '').replace('-', '')
        
        if not number.isdigit():
            return False
        
        digits = [int(d) for d in number]
       
        if len(digits) < 13:
            return False
        else:
            return True

    def is_credit_card_expired(self, expiration_date):
        
        expiration_date = datetime.strptime(expiration_date,'%m/%y')
        
        today = datetime.today()
        
        if expiration_date <= today:
            return True
        else:
            return False

    def is_valid_phone_number(self,phone_number):
        if not phone_number.isdigit():
            return False
        
        if len(phone_number) != 10:
            return False
        
        return True

    def is_valid_CVV(self, cvv):
        if not cvv.isdigit():
            return False
        
        if len(cvv) != 3:
            return False
        
        return True

class SuccessPage:
    def __init__(self, booking):
        self.__root = ctk.CTk()
        self.__root.title("Summary")
        self.__root.geometry("420x200+280+280")
        lab1 = Label(self.__root, text="Your booking id is " + f"{booking['_id']}",font=100)
        lab1.place(x=140,y=95)
        lab2 = Label(self.__root, text="Thank you for your reservation",font=100)
        lab2.place(x=125,y=40)
        btn1 = Button(self.__root, text="Home",font=100, command= lambda:self.go_first_page())
        btn1.place(x=230,y=140)
        
        self.__root.mainloop()
        
    def go_first_page(self):
        self.__root.destroy()
        MainApp()


class ShowRoomPage(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Room Catalog")
        self.geometry("1250x720")
        self.minsize(1200 ,600)
        ctk.set_widget_scaling(1.5)

        self.grid_columnconfigure((0, 1, 2, 3), weight=1)
        self.grid_rowconfigure((0, 1, 2, 3), weight=1)

        self.tabview = ctk.CTkTabview(self, width=1000, height=400)
        self.tabview.grid(row=0, column=0, padx=20, pady=5, sticky="nsew", columnspan=4, rowspan=2)
        self.tabview.add("Kirimayaresort")
        self.tabview.add("Muthimaya")
        self.tabview.add("Atta")
        self.tabview.tab("Kirimayaresort").grid_columnconfigure(0, weight=1)  # configure grid of individual tabs
        self.tabview.tab("Muthimaya").grid_columnconfigure(0, weight=1)
        self.tabview.tab("Atta").grid_columnconfigure(0, weight=1)

        self.Stays_scrollable_frame = ctk.CTkScrollableFrame(master=self.tabview.tab('Kirimayaresort'), height=320)
        self.Stays_scrollable_frame.grid(row=0, column=0, sticky="nsew", padx=10)
        self.Stays_scrollable_frame.grid_columnconfigure(0, weight=1)

        self.Rooms_scrollable_frame = ctk.CTkScrollableFrame(master=self.tabview.tab('Muthimaya'), height=320)
        self.Rooms_scrollable_frame.grid(row=0, column=0, sticky="nsew", padx=10)
        self.Rooms_scrollable_frame.grid_columnconfigure(0, weight=1)

        self.Suites_scrollable_frame = ctk.CTkScrollableFrame(master=self.tabview.tab('Atta'), height=320)
        self.Suites_scrollable_frame.grid(row=0, column=0, sticky="nsew", padx=10)
        self.Suites_scrollable_frame.grid_columnconfigure(0, weight=1)
        
        room1 = PhotoImage(file="PICTURE/PLANTATION.png")
        room1pic = room1.subsample(1, 1)
        room2 = PhotoImage(file="PICTURE/HORIZON.png")
        room2pic = room2.subsample(1, 1)
        room3 = PhotoImage(file="PICTURE/MUTHIMAYA.png")
        room3pic = room3.subsample(1, 1)
        room4 = PhotoImage(file="PICTURE/ONEBEDROOMSUITE.png")
        room4pic = room4.subsample(1, 1)
        room5 = PhotoImage(file="PICTURE/ONEBEDROOMDELIGHT.png")
        room5pic = room5.subsample(1, 1)
        room6 = PhotoImage(file="PICTURE/ONEBEDROOMDELIGHT.png")
        room6pic = room6.subsample(1, 1)
        room7 = PhotoImage(file="PICTURE/PENTHOUSESUITE.png")
        room7pic = room7.subsample(1, 1)
        

        room_pics = [room1pic, room2pic, room3pic, room4pic, room5pic, room6pic, room7pic]
        room_names = [r.room_plantationview1, r.room_horizonview, r.room_muthimaya_forest_poolvilla, r.room_one_bedroom_suite, r.room_one_bedroom_delight, r.room_two_bedroom_delight, r.room_penthouse_suite]

        for i in range(2):
            frame = ctk.CTkScrollableFrame(master=self.Stays_scrollable_frame, width=850, orientation='horizontal')
            frame.grid(row=i, column=0, padx=20, pady=10)
            ctk.CTkLabel(master=frame, image=room_pics[i], text='').grid(row=0, column=0, padx=20)
            ctk.CTkLabel(master=frame, text=str(room_names[i]), justify='left').grid(row=0, column=1, padx=20, pady=20)

        for i in range(1):
            frame = ctk.CTkScrollableFrame(master=self.Rooms_scrollable_frame, width=850, orientation='horizontal')
            frame.grid(row=i , column=0, padx=20, pady=10)
            ctk.CTkLabel(master=frame, image=room_pics[i+2], text='').grid(row=0, column=0, padx=20)
            ctk.CTkLabel(master=frame, text=str(room_names[i+2]), justify='left').grid(row=0, column=1, padx=20, pady=20)

        for i in range(len(room_pics) - 3):
            frame = ctk.CTkScrollableFrame(master=self.Suites_scrollable_frame, width=850, orientation='horizontal')
            frame.grid(row=i + 3, column=0, padx=20, pady=10)
            ctk.CTkLabel(master=frame, image=room_pics[i + 3], text='').grid(row=0, column=0, padx=20)
            ctk.CTkLabel(master=frame, text=str(room_names[i + 3]), justify='left').grid(row=0, column=1, padx=20, pady=20)

        back_button = ctk.CTkButton(self, text="Back", command=lambda:self.back())
        back_button.grid(row=2, column=3, columnspan=2)


        self.mainloop()
    


    def back(self):
        self.destroy()
        MainApp()
        
class SelectRoomPage(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Select Room")
        self.geometry("1250x720")
        self.minsize(1200 ,600)

        self.grid_columnconfigure((0, 1, 2, 3, 4), weight=1)
        self.grid_rowconfigure((0, 1, 2, 3, 4), weight=0)
        ctk.set_widget_scaling(1.2)


        self.check_in_label = ctk.CTkLabel(self, text="Check-in Date")
        self.check_in_label.grid(column=0, row=2)

        self.check_in_cal = Calendar(master=self, background='#2f3640',selectmode = 'day', year = 2023, month = 5, day = 2)
        self.check_in_cal.grid(row=1 ,column=0 ,padx=50)

        self.check_out_label = ctk.CTkLabel(self, text="Check-out Date")
        self.check_out_label.grid(row=2, column=4)
        
        self.check_out_cal = Calendar(master=self, background='#2f3640',selectmode = 'day', year = 2023, month = 5, day = 4)
        self.check_out_cal.grid(row=1 , column=4, padx=40)

        test = ShowRoomPage()




class MainApp:
    def __init__(self):
        global temp
        self.__mainapp = ctk.CTk()
        self.__mainapp.title("Kirmaya")
        self.__mainapp.geometry("400x320")
        self.temp = []
        img = PhotoImage(file='PICTURE/KIRIMAYA.png')

        Label(self.__mainapp, image=img).place(x=115,y=50)
        btn = Button(self.__mainapp, text="Book a room", command=lambda: self.go_bookrooom(),font=30)
        btn.place(x=180, y=170)
        btn = Button(self.__mainapp, text="All room", command=lambda: self.go_showroom(),font=30)
        btn.place(x=200, y=220)
        btn2 = Button(self.__mainapp, text="View booking", command=lambda: self.go_view_booking(),font=30)
        btn2.place(x=180, y=270)
        self.__mainapp.mainloop()
        
    def go_bookrooom(self):
        self.__mainapp.destroy()
        SearchPage()
    
    def go_showroom(self):
        self.__mainapp.destroy()
        ShowRoomPage()

    def go_view_booking(self):
        
        self.root = Toplevel()
        self.root.title("Detail")
        self.root.geometry("420x200+280+280")

        self.booking_id = StringVar()
        Label(self.root, text="Please enter your booking id",font=20).place(x=80,y=10)
        id_entry = Entry(self.root, textvariable=self.booking_id, font = 20,width=13 )
        id_entry.place(x=100,y=50)
        btn = Button(self.root, text="Confirm",bg="green",command= lambda: self.find_booking())
        btn.place(x=260,y=50)


        self.root.mainloop()

    def find_booking(self):
        API_ENDPOINT3 = "http://127.0.0.1:8000/book_history"
        payload = { "id" : int(self.booking_id.get())}
        response = requests.post(API_ENDPOINT3, json=payload)
        
        for label in self.temp:
            label.destroy()

        
        if response.ok:
            data = response.json()
            data = data['Data']
            if data == 1:
                print("444")
                lab = Label(self.root, text="Not valid id",fg=("red"))
                lab.place(x=260,y=80)
                self.temp.append(lab)

            else:
                print(data)
                print(type(data))
                data2 = data['_room']
                data2 = data2['_room_name']
                data = data['_interval']
                date_in = datetime.fromisoformat(f"{data['_date_start']}")
                date_in = date_in.strftime('%d/%m/%y')
                date_end = datetime.fromisoformat(f"{data['_date_end']}")
                date_end = date_end.strftime('%d/%m/%y')
                print(date_in)
                print(date_end)
                print(data2)
                lb1= Label(self.root, text=date_in + " to "+ date_end,font=20)
                lb1.place(x=80,y=100)
                lb2=Label(self.root, text=data2,font=20)
                lb2.place(x=80,y=140)
                self.temp.append(lb1)
                self.temp.append(lb2)

            
if __name__ == "__main__":
    app = MainApp()
    