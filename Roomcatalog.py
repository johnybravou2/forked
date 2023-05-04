from datetime import datetime
from Room import Room
from Interval import Interval
from Booking import Booking
class Roomcatalog:
    def __init__(self):
        self._room_lists = []
        self._check = True

    def add_room(self,room):
        self._room_lists.append(room)

    def show_catalog(self):
        for i in self._room_lists:
            print(i._room_name)
    
    def find_available_room(self, start_date, end_date, hotel):
        start_time = "12:00"
        end_time = "11:00"
        date1 = datetime.strptime(start_date + " " + start_time, '%d-%m-%Y %H:%M')
        date2 = datetime.strptime(end_date + " " + end_time, '%d-%m-%Y %H:%M')
        available_room = []
        #available_room_all = {}
        #j = 0
        for i in self._room_lists:
            if not i.room_available(date1, date2) and i._hotel_name == hotel:
                continue
            if not i._hotel_name == hotel:
                continue
            available_room.append(i)
            # available_bathroom.append(i._number_of_bathroom)
            #available_room_all[j] = [i._room_name,i._number_of_bathroom]
            #j += 1
        return available_room
    
    def add_to_cart(self, room, tempcart):
        for i in self._room_lists:
            if i._room_name == room:
                add_room = i
                break
        
        tempcart.add_room_Cart(add_room)

    def remove_from_cart(self, room, tempcart):
        for i in self._room_lists:
            if i._room_name == room:
                remove_room = i
                break
        
        tempcart.remove_from_cart(remove_room)

    def book_room(self, room, st_date, end_date, user, book_his):
        
        for i in self._room_lists:
            if i._room_name == room:
                book_room = i
                print('#############')
                break
        interval = Interval(st_date, end_date)
        
        book_room.add_interval(interval)
        booking = Booking(book_room,interval,user)
        book_his.append(booking)
        
        print(booking)
        return booking