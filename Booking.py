import datetime
import uuid
from Room import Room
from Interval import Interval

class Booking:
    existng_booking_id= set()
    id = 0

    def __init__(self,room,interval):
        Booking.id += 1
        self._room = room
        self._interval = interval
        self._id = Booking.id
        #self.__day_range = interval
        #self.__day_start = self.__day_range.get_end_time()
        #self.__day_end = self.__day_range.get_start_time()
        #self.__price = room.get_room_amount() *(self.__day_start - self.__day_end).days
        #self._booking_id = self.generate_booking_id()

    def generate_booking_id(cls):
        while True:
            booking_id = str(uuid.uuid4().hex)[:8]
            if booking_id not in cls.existing_booking_ids:
                cls.existing_booking_ids.add(booking_id)
                return booking_id
        
 #เเก้คิดเงินหน่อยค้าบ
    def show_booking(self):
        print(self.__day_start)
        print(self.__day_end)
        print(self.__price)

    def __str__(self):
        m_str = "Room: " + str(self._room)
        m_str += "ID: " + str(self._id)
        m_str += " Time : " + self._interval.__str__()
        return m_str