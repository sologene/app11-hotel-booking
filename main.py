import pandas as pd
df = pd.read_csv("hotels.csv", dtype={"id":str})


class Hotel:
    def __init__(self,hotel_id):
        self.hotel_id = hotel_id
        self.name = df.loc[df["id"] == self.hotel_id, "name"].squeeze()
    def book(self):
        df.loc[df["id"] == self.hotel_id, "available"] = "no"
        df.to_csv("hotels.csv", index=False)
    def available(self):
        availability = df.loc[df["id"] == self.hotel_id, "available"].squeeze()
        if availability == "yes":
            return True
        else:
            return False

    def view_hotels(self):
        pass


class Ticket:
    def __init__(self,customer_name,hotel_object):
        self.customer_name = customer_name
        self.hotel = hotel_object
    def generate(self):
        content = f"""
    Thank you for your reservation!
    Here is your booking data:
    Name:{self.customer_name}
    Hotel Name: {self.hotel.name}
    """
        return content

class CreditCard:
     def __init__(self,number,expiration,holder,cvc):
         self.number = number

     def validate(self,expiration, holder, cvc)




print(df)
id = input("Enter the id of the hotel:")
hotel = Hotel(id)

if hotel.available():
    credit_card = CreditCard(number="1234567890123456" )
    if credit_card.validate(expiration="12/26", holder="John Smith",cvc="123")
        hotel.book()
        name = input("Enter your name: ")
        ticket = Ticket(name, hotel)
        print(ticket.generate())
    else:
        print("There was a problem with your payment")
else:
    print("Hotel is not free")