class Cart:
    def __init__(self):
        self.__room_list = []
        self.__total_price = 0
        
    def add_room_Cart(self, room):
        self.__room_list.append(room)
        print(len(self.__room_list))
        self.__update()

    def clear_cart(self):
        self.__room_list = []
        self.__update()

    def remove_from_cart(self, room):
        r=0
        j=0
        for i in self.__room_list:
            if i == room:
                r = j
                break
            j+=1
        
        self.__room_list.pop(r)
        self.__update()

    def get_room(self):
        return self.__room_list
    
    def __update(self):
        self.__total_price = 0
        for room in self.__room_list:
            room_price = room.room_price 
            self.__total_price += room_price
        return True

    @property
    def total_price(self):
        return self.__total_price

    @property
    def room_list(self):
        return self.__room_list

    def show_item(self):
        res = []
        for reserved in self.__room_list:
            res.append(reserved._room_name)
        return res
    
    #def __str__(self):
     #   return (f"Room name : {self._room_name } , Hotel name : {self._hotel_name}")


