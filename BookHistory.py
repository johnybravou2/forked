class BookHistory:
    def __init__(self):
        self.__history_list = []
        
    def add_book_history (self,booking):
        self.__history_list.append(booking)