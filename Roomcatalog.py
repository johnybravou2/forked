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
    
        for i in self._room_lists:
            if not i.room_available(date1, date2) and i._hotel_name == hotel:
                continue
            if not i._hotel_name == hotel:
                continue
            available_room.append(i)
           
        return available_room
    

    def book_room(self, room, st_date, end_date, user, bookhis):
        
        for i in self._room_lists:
            if i._room_name == room:
                book_room = i

                break
        interval = Interval(st_date, end_date)
        
        book_room.add_interval(interval)
        booking = Booking(book_room,interval,user)
        bookhis.add_book_history(booking)
        #user.add_booking(booking)
        print(booking)
        
        return booking