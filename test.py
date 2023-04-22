import datetime
from Roomcatalog import Roomcatalog
from room import Room
from Booking import Booking
from account import customer
from account import admin
from Interval import interval
from fastapi import FastAPI
from Cart import Cart

app = FastAPI()

room_plantationview = Room("Kirimayaresort",
                           "Plantation View",
                           "42 sq. m.",
                           "1 Bedroom",
                           "1 Room",
                            "2000",
                            "PICTURE\PLANTATION.png")
room_horizonview = Room("Kirimayaresort",
                        "Horizon View",
                        "42 sq. m.",
                        "1 Bedroom",
                        "1 Room",
                        "3000",
                        "PICTURE\HORIZON.png"
                        ) 

room_muthimaya_forest_poolvilla = Room("Muthimaya",
                                        "MUTHI MAYA Forest Pool Villa",
                                       "164 sq. m.",
                                       "1 Bedroom",
                                       "1 Room",
                                       
                                       "2500",
                                       "PICTURE\MUTHIMAYA.png")

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

start_date= "19-6-2023"
start_time=  "12:30"
testalog = Roomcatalog()

testalog.add_room(room_plantationview)
testalog.add_room(room_horizonview)
testalog.add_room(room_muthimaya_forest_poolvilla)

room_plantationview.add_interval(interval(datetime.datetime(2023, 6, 10, 10, 0),datetime.datetime(2023, 6, 17, 10, 0)))
room_horizonview.add_interval(interval(datetime.datetime(2023, 6, 10, 10, 0),datetime.datetime(2023, 6, 11, 10, 0)))


for i in room_plantationview._date_not_available: 
    print(i.get_start_time())
    print(i.get_end_time())

a_room = testalog.find_available_room("12-6-2023","0:00","14-6-2023","0:00","Kirimayaresort")

for i in a_room:
    print(i)

# date1 = datetime.datetime(2023, 4, 5, 12, 0)
# date2 = datetime.datetime(2023, 4, 7, 12, 0)
# timediff = date2 - date1
# print(timediff.days)
# amount = 3000
# price = timediff.days * amount
# print(price)

@app.get("/", tags=['root'])
async def root() -> dict:
    return {"Ei": "Ei"}


@app.post("/show_available_room", tags=["book room"])
async def show_available_room(data:dict)->dict:
    hotel = data["Hotel"]
    st_d = data["start_date"]
    st_t = data["start_time"]
    end_d = data["end_date"]
    end_t = data["end_time"]

    a_room = testalog.find_available_room(st_d,st_t,end_d,end_t,hotel)
    for i in a_room:
        print(i)
    dt = {}
    for i in a_room:
        dt[i._room_name] = i._room_pic
    print(dt)
    return {"Data": dt}
    #return {"Data": a_room}

@app.get("/",tags=["Cart"])
async def cart() -> dict :
    return("Ping":"Pong")

@app.post("/add_room_cart",tags=["Cart"])
async def add_room_Cart(data:dict) -> dict :
    room = data["Room"]
