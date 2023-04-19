from datetime import *
class Interval:
    def __init__(self,start_date_str,start_time_str,end_date_str,end_time_str):
        self._date_start = self.convert_str_to_datetime(start_date_str, start_time_str)
        self._date_end = self.convert_str_to_datetime(end_date_str, end_time_str)
    
    def convert_str_to_datetime(self, str_date, str_time):
        return datetime.strptime(str_date + " " + str_time, '%d-%m-%Y %H:%M')
    
    def convert_datetime_to_str(self, datetime):
        return datetime.strftime("%m/%d/%Y, %H:%M")
    
    def get_start_time (self):
        return self._date_start
    
    def get_end_time (self):
        return self._date_end