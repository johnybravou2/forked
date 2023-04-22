import datetime
import uuid
from Room import Room
from Interval import Interval

class Booking:
    existng_booking_id= set()

    def __init__(self,room:Room,interval:Interval):
        self.__day_range = interval
        self.__day_start = self.__day_range.get_end_time()
        self.__day_end = self.__day_range.get_start_time()
        self.__price = room.get_room_amount() *(self.__day_start - self.__day_end).days
        self._booking_id = Booking.generate_booking_id()

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
