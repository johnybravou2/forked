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
    
    def find_available_room(self, start_date, start_time, end_date, end_time, hotel):
        date1 = datetime.strptime(start_date + " " + start_time, '%d-%m-%Y %H:%M')
        date2 = datetime.strptime(end_date + " " + end_time, '%d-%m-%Y %H:%M')
        available_room = []
        available_room_all = {}
        j = 0
        for i in self._room_lists:
            if not i._status_available and i._hotel_name == hotel:
                continue
            if not i.room_available(date1, date2) and i._hotel_name == hotel:
                continue
            if not i._hotel_name == hotel:
                continue
            available_room.append(i)
            # available_bathroom.append(i._number_of_bathroom)
            available_room_all[j] = [i._room_name,i._number_of_bathroom]
            j += 1
        return available_room
    
    def book_room(self, room, user, st_date, end_date):
        
        for i in self._room_lists:
            if i._room_name == room:
                book_room = i
                break
        interval = Interval(st_date, end_date)
        book_room.add_interval(interval)
        booking = Booking()
        
        
        return "success"