from tkinter import *
from tkinter.font import *
import tkinter.messagebox
import requests
import json
#from cataloggui import CarCatalogTK


class LoginGUI:
    def __init__(self):
        self.token = ""
        self.__login = Tk()
        #font
        self.__header_font = Font(family="Kanit", weight="bold", size=20)
        self.__normal_font = Font(family="Kanit", weight="normal", size=16)
        self.__txtbox_font = Font(family="Kanit", weight="normal", size=12)
        self.__login.title("Login")
        self.__login.geometry("350x200")
        self.__login.resizable(width=False, height=False)
        Label(text="Login", font=self.__header_font).pack(anchor="center")
        Label(text="Username:", font=self.__normal_font).place(x=25, y=50)
        self.__username_entry = Entry(self.__login, font=self.__txtbox_font)
        self.__username_entry.place(x=130, y=50)
        Label(text="Password:", font=self.__normal_font).place(x=25, y=80)
        self.__pwd_entry = Entry(self.__login, font=self.__txtbox_font, show="*")
        self.__pwd_entry.place(x=130, y=80)
        Button(text="Login", font=self.__normal_font, command=self.login).place(x=140, y=120)
        self.__login.mainloop()
        
        
   
    def login(self):
        if self.__username_entry.get() != "" and self.__pwd_entry.get() != "":
            url = "http://127.0.0.1:8000/token"
            print(url)
            r = requests.post(url,{"username":self.__username_entry.get(),"password":self.__pwd_entry.get()},headers = {"Content-Type":"application/x-www-form-urlencoded"})
            # r = requests.post(url,{"username":"petch","password":"5678"},headers = {"Content-Type":"application/x-www-form-urlencoded"})
            print(r)
            data = json.loads(r.text)
            print(data)
            if r.status_code == 200 :
                self.token = data["access_token"]
                if self.token == '':
                    tkinter.messagebox.showerror(title="Error", message="Not Correct!!!!")
                else:
                    tkinter.messagebox.showinfo(title="Success", message="Correct!! Welcome To My Shop")
                    self.__login.destroy()
                    #CarCatalogTK(self.token)
        else:
            tkinter.messagebox.showerror(title="Error", message="Please Enter Username And Password")

gui = LoginGUI()