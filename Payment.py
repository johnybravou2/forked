

class CreditCard:
    def __init__(self, card_number, card_holder, expiration_date, cvv, balance):
        self.card_number = card_number
        self.card_holder = card_holder
        self.expiration_date = expiration_date
        self.cvv = cvv
        self.balance = balance

    def authorize_payment(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            return True
        else:
            return False