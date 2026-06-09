# Parent class
class Ticket:
    def price(self):
        print("Ticket Price: ₹150")

# Child class
class VIPTicket(Ticket):
    def price(self):
        print("Ticket Price: ₹500")

# Create object of VIPTicket
ticket = VIPTicket()
ticket.price()