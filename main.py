from Room import Room
from datetime import *
from fastapi import FastAPI
import random
from account import*

from Interval import*
from Roomcatalog import Roomcatalog
from Booking import BookHistory


from System import *
from account import User
app = FastAPI()

room_plantationview1 = Room("Kirimayaresort",
                           "Plantation View",
                           "1101",
                           "42 sq. m.",
                           "1 Bedroom",
                           "1 Room",
                            2990,
                            "PICTURE\PLANTATION.png")
#room_plantationview2 = Room("Kirimayaresort",
#                           "Plantation View",
#                           "1102",
#                           "42 sq. m.",
#                           "1 Bedroom",
#                           "1 Room",
#                            2000,
#                            "PICTURE\PLANTATION.png")
room_horizonview = Room("Kirimayaresort",
                        "Horizon View",
                        "1201",
                        "48 sq. m.",
                        "1 Bedroom",
                        "1 Room",
                        3990,
                        "PICTURE\HORIZON.png"
                        ) 

room_muthimaya_forest_poolvilla = Room("Muthimaya",
                                        "MUTHI MAYA Forest Pool Villa",
                                        "103",
                                       "164 sq. m.",
                                       "1 Bedroom",
                                       "1 Room",
                                       
                                       2590,
                                       "PICTURE\MUTHIMAYA.png")

##atta

room_one_bedroom_suite = Room("Atta",
                              "One Bedroom Suite",
                              "1005",
                              
                              "65 sq. m.",
                              "1 Bedroom",
                              "1 Room",
                              
                              4990,"PICTURE\ONEBEDROOMSUITE.png")

room_one_bedroom_delight = Room("Atta",
                                "One Bedroom Delight",
                                "1006",
                                
                                "65 sq. m.",
                                "1 Bedroom",
                                "1 Room",
                                
                                4990,"PICTURE\ONEBEDROOMDELIGHT.png")

room_two_bedroom_delight = Room("Atta",
                                "Two Bedroom Delight",
                                "1007",
                                
                                "102 sq. m.",
                                "2 Bedroom",
                                "2 Room",
                                
                                5990,"PICTURE\ONEBEDROOMDELIGHT.png")

room_penthouse_suite = Room("Atta",
                            "Penthouse Suite",
                            "1008",
                            
                            "235 sq. m.",
                            "2 Bedroom",
                            "2 Room",
                            
                            9990,"PICTURE\PENTHOUSESUITE.png")
mix = customer("mix",
               "saranji",
               "0627370763",
               "mixsaranji",
               "mix1234") 

xiw = admin("xiw",
            "tarijnaras",
            "0950988592",
            "xiwijnaras",
            "xiw1234")

sym = System()
testalog = Roomcatalog()
bookhis = BookHistory()

testalog.add_room(room_plantationview1)
#testalog.add_room(room_plantationview2)
testalog.add_room(room_horizonview)
testalog.add_room(room_muthimaya_forest_poolvilla)
testalog.add_room(room_one_bedroom_suite)
testalog.add_room(room_one_bedroom_delight)
testalog.add_room(room_two_bedroom_delight)
testalog.add_room(room_penthouse_suite)

room_plantationview1.add_interval(Interval("1-6-2023","10-6-2023"))
room_horizonview.add_interval(Interval("5-6-2023","10-6-2023"))

print(datetime.now())
print(room_horizonview._date_not_available.__str__())
print(bookhis.show_booking(1))

sym.add_user(mix)
sym.add_user(xiw)

#function หาuser


#         "car": "ABZW-999",
#   "start_date": "11-6-2018",
#   "start_time": "9:00",
#   "end_date": "12-6-2018",
#   "end_time": "9:59"
# HOME
@app.get("/")
async def home():
    return {"EiEi"}






#Cars
@app.get("/Rooms", tags=["Catalog"])
async def home():
    return {"Data": testalog._room_lists}

    return {"catalog":[{"hotel_name": x.get_hotel_name(),
                        "room_number": x.get_car_model(),
                        "room_name": x.get_room_name(),
                        "room_area": x.get_room_area(),
                        "room_amount": x.get_room_amount()}
                       for x in testalog._room_lists]}

#Add_book
@app.post("/add_room", tags=["Room"])
async def add_room_to_catalog(data:dict)->dict:
    


    testalog.add_room(Room(
            data['hotel'],
            data['room name'],
            data['room number'],
            data['room area'],
            data['number_of_bathroom'],
            data['number_of_bedroom'],
            data['room_price'],
            data['room pic'])
        )




@app.post("/show_available_room", tags=["Search room"])
async def show_available_room(data:dict)->dict:
    
    hotel = data["Hotel"]
    st_d = data["start_date"]
    end_d = data["end_date"]
    
    a_room = testalog.find_available_room(st_d,end_d,hotel)
    print(a_room)
    for i in a_room:
        print(i)
    
    return {"Data": a_room}
    #return {"Data": a_room}





@app.post("/book_room",tags = ["Booking"])
async def booking_room(data: dict) -> dict:
    #current_user._booking = testalog.book_room(data.room,data.start_date,data.end_date)
    room_name = data['room']
    st_date = data['start_date']
    end_date = data['end_date']
    title = data['title']
    name = data['name']
    surname = data['surname']
    email = data['email']
    phone_number = data['phone_number']
    user = User(title, name, surname, email, phone_number)
    sym.add_user(user)

    return {"Data" : testalog.book_room(room_name,st_date,end_date,user,bookhis)}


@app.post("/book_history",tags = ["Booking"])
async def show_book(data: dict) -> dict:
    booking_id = data['id']
    
    if bookhis.show_booking(booking_id) == 1:
        print('1')
        return {"Data": 1}
    

    #booking = bookhis.show_booking(booking_id)
    #print(f"{booking['_interval']}")
    return{"Data": bookhis.show_booking(booking_id)}

##### CREDIT ###### E D I T I N G
#@app.post("/add_credit_info", tags=["CreditCard"])
#async def add_credit_info(data:CreditCard,current_user= Depends(sym.get_current_user)):
#    current_user.add_credit_info(CreditInfo(data.exprie_card,data.card_number,data.security_credit))
#    return current_user._credit_card
#
#@app.post("/edit_credit_info", tags=["CreditCard"])
#async def edit_credit_info(data:CreditCard,current_user= Depends(sym.get_current_user)):
#    current_user._credit_card.edit_credit_info(data.exprie_card,data.card_number,data.security_credit)
#    return current_user._credit_card
#
#
#
#@app.get("/Payment",tags =["Payment"])
#async def make_payment(current_user = Depends(sym.get_current_user)):
#    status = False
#    transaction_id = random.randint(100000000,999999999)
#    rental_price = current_user._booking.get_price()
#    credit_info = current_user._credit_card
#    payment = Payment(rental_price,status,transaction_id,credit_info)
#    return payment
#
#
## @app.post("/watch ",tags = ["Favourite"])
## async def add_favourite(data:FavouriteDTO):
##     petch.add_fav_car(data.car)
##     return {"status":"Success"}
#    
#    
#
#
##Credit_Card
#
#Payment


