import datetime

class Room:
    def __init__(self, hotel_name, room_name, room_area, number_bedroom, number_bathroom, room_amount ,room_pic):
        self._hotel_name = hotel_name
        self._room_name = room_name
        self._room_area = room_area
        self._number_of_bathroom = number_bedroom
        self._number_of_bedroom = number_bathroom
        self._date_not_available = []
        self._room_amount = room_amount
        self._room_pic = room_pic
        self._status_available = True

    def add_interval(self, interval):
        self._date_not_available.append(interval)

    def check_no_overlap(self,start_time1, end_time1, start_time2, end_time2):
        if start_time1 > end_time2 or start_time2 > end_time1:
            return True
        else:
            return False

    def room_available(self, datetime1, datetime2):
        for i in self._date_not_available:
            if not self.check_no_overlap(i.get_start_time(), i.get_end_time(), datetime1, datetime2):
                return False
        return True
    
    def get_hotel_name(self):
        return self._hotel_name
    
    def get_room_name(self):
        return self._room_name
    
    def __str__(self):
        return(f"Room name : {self._room_name } , Hotel name : {self._hotel_name}")