class CreditInfo: 
    def __init__(self,expire_card,card_number,security_credit): 
        self.__expire_card = expire_card 
        self.__card_number = card_number 
        self.__security_credit = security_credit 

    def get_expire_card(self):
        return self.__expire_card
    
    def set_expire_card(self, new_expire_card):
        self.__expire_card = new_expire_card

    def get_card_number(self):
        return self.__card_number
    
    def set_card_number(self, new_card_number):
         self.__card_number = new_card_number

    def get_security_credit(self):
        return self.__security_credit
    
    def set_security_credit(self, new_security_credit):
        self.__security_credit = new_security_credit


    def edit_credit_info(self,new_expire_card,new_card_number,new_security_credit):
        if isinstance(new_expire_card, str):
            self.expire_card = new_expire_card
        if isinstance(new_card_number, str):
            self.card_number = new_card_number
        if isinstance(new_security_credit, str):
            self.security_credit = new_security_credit

    expire_card = property(get_expire_card, set_expire_card)
    card_number = property(get_card_number, set_card_number)
    security_credit = property(get_security_credit, set_security_credit)