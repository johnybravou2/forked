from Roomcatalog import Roomcatalog
from CreditCard import CreditInfo
import datetime
from Room import *
#class User:
#    def __init__(self,contact_name,contact_username,contact_phone_num,contact_email,contact_password):
#        self._contact_name= contact_name
#        self._contact_username = contact_username
#        self._contact_phone_num = contact_phone_num
#        self._contact_email = contact_email
#        self._contact_password = contact_password
#
#    def watch_room(self, Roomcatalog, hotel_name, datetime1, datetime2):
#        tamp_rooms_lists = []
#        for i in Roomcatalog._room_lists:
#            if hotel_name == "Kirimayaresort" and i._hotel_name == "Kirimayaresort" and i.room_available(datetime1,datetime2):
#                tamp_rooms_lists = [room for room in Roomcatalog._room_lists if room.get_hotel_name() == "Kirimayaresort" ]
#                return tamp_rooms_lists 
#            elif hotel_name == "Muthimaya" and i._hotel_name == "Muthimaya" and i.room_available(datetime1,datetime2):
#                tamp_rooms_lists.append(i)
#                return tamp_rooms_lists
#            elif hotel_name == "Atta" :
#                tamp_rooms_lists = [room for room in Roomcatalog._room_lists if room.get_hotel_name() == "Atta" ]
#                return tamp_rooms_lists

class User:
    def __init__(self, title, name, surname, email, phone_number) :
        self._title = title
        self._name = name
        self._surname = surname
        self._email = email
        self._phone_number = phone_number


class customer(User):
    def __init__(self, contact_name, contact_username, contact_phone_num, contact_password, contact_email):
        super().__init__(contact_name, contact_username, contact_phone_num, contact_password, contact_email)

    def select_room(self,room):
        self._choose_room=room    

    def search_room(self,):
        pass

class admin(User):
    def __init__(self, contact_name, contact_username, contact_phone_num, contact_password, contact_email):
        super().__init__(contact_name, contact_username, contact_phone_num, contact_password, contact_email)

    def add_room(self,room,room_catalog:Roomcatalog):
        room_catalog._room_lists.append(room)

        
mix = customer("mix",
               "saranji",
               "0627370763",
               "mixsaranji",
               "mix1234") 

xiw = admin("xiw",
            "tarijnaras",
            "0950988592",
            "xiwijnaras",
            "xiw1234")
# class Owner(Contact):
#     def __init__(self, contact_name, contact_username, contact_phone_num, contact_password, contact_email):
#         super().__init__(contact_name, contact_username, contact_phone_num, contact_password, contact_email)          
#     def edit_profile(self,new_name,new_username,new_phone_num,new_password,new_email):
#         if isinstance(new_name, str):
#             self._contact_name = new_name
#         if isinstance(new_username, str):
#             self._contact_username = new_username
#         if isinstance(new_phone_num, str):
#             self._contact_phone_num = new_phone_num
#         if isinstance(new_password, str):
#             self._contact_password = new_password
#         if isinstance(new_email, str):
#             self._contact_email = new_email
        
        
# class Renter(Contact):
#     def __init__(self, contact_name, contact_username, contact_phone_num, contact_password, contact_email):
#         super().__init__(contact_name, contact_username, contact_phone_num, contact_password, contact_email)
#         self._list_favour = []
#         self._credit_card = None
#         self._list_history = []
#         self._booking = None

#     def add_fav_car(self,car):
#         self._list_favour.append(car)
#     def watch_fav_car(self):
#         for car in self._list_favour:
#             print(car.get_car_brand())
#             print(car.get_car_model())
#             print(car.get_car_date_not_avalible())
#             #โชว์ค่า fav car ออกมา
#     def edit_profile(self,new_name,new_username,new_phone_num,new_password,new_email):
#         if isinstance(new_name, str):
#             self._contact_name = new_name
#         if isinstance(new_username, str):
#             self._contact_username = new_username
#         if isinstance(new_phone_num, str):
#             self._contact_phone_num = new_phone_num
#         if isinstance(new_password, str):
#             self._contact_password = new_password
#         if isinstance(new_email, str):
#             self._contact_email = new_email
    
#     #credit methods
#     def add_credit_info(self, creditInfo:CreditInfo):
#         self._credit_card = creditInfo
 