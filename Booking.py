import datetime
import uuid
from Room import Room
from Interval import Interval

class Booking:
    existng_booking_id= set()
    id = 100000

    def __init__(self, room, interval, user):
        Booking.id += 1
        self._room = room
        self._interval = interval
        self._id = Booking.id
        self._user = user



        
 

    def __str__(self):
        m_str = "Room: "+ str(self._room)
        m_str += " ID: " + str(self._id)
        m_str += " Time : " + self._interval.__str__()
        return(f"room: {self._room._room_name}  Time: {self._interval.__str__()} id: {self._id}")
        return m_str
    
class BookHistory:
    def __init__(self):
        self.__history_list = []
        
    def add_book_history(self,booking):
        self.__history_list.append(booking)

    def show_booking(self,id):
        for i in self.__history_list:
            if i._id == id:
                booking = i
                return booking
        return 1

