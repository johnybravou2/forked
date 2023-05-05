from Roomcatalog import Roomcatalog
import datetime
from Room import *
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
