import uuid
class Payment:
    transaction_id = 1
    def __init__(self, amount):
        self.amount = amount
        self.transaction_ID = None

    def process_payment(self, card):
        if card.authorize_payment(self.amount):
            self.transaction_id = self.generate_transaction_id()
            return f"Payment successful. Transaction ID: {self.transaction_id}"
        else:
            return "Payment failed."
    
    def generate_transaction_id(self):
        return str(uuid.uuid1())

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