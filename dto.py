from pydantic import BaseModel

class AvalibleDTO(BaseModel):
    Hotel : str
    start_date : str
    start_time : str
    end_date : str
    end_time : str
    
class BookingDTO(BaseModel):
    room : str
    start_date : str
    end_date : str

class EditProfileDTO(BaseModel):
    new_name :str
    new_username :str
    new_phone_num :str
    new_password :str
    new_email :str
    
class CreditCard(BaseModel):
    exprie_card:str
    card_number:str
    security_credit:str    
    
class AddroomDTO (BaseModel):
    hotel_name : str
    room_number : int
    room_name : str
    room_area : int
    number_of_bathroom : int
    number_of_bedroom : int
    room_amount : int
    
class Registeration(BaseModel):
    contact_name : str
    contact_username : str
    contact_phone_num : str
    contact_email : str
    contact_password : str