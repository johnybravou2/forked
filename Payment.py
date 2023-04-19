class Payment: 
    def __init__(self,payment_status,transaction_id,amount,card_info): 
        self.__payment_status = payment_status 
        self.__transaction_id = transaction_id 
        self.__amount = amount 
        self.__card_info = card_info
        
    def payment(self):
        pass