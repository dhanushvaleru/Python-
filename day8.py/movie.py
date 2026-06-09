class Customer:
    def __init__(self, customer_name):
        self.customer_name = customer_name
class Movie:
    def __init__(self, movie_name, ticket_price):
        self.movie_name = movie_name
        self.ticket_price = ticket_price
class Booking:
    def __init__(self, customer, movie, number_of_tickets):
        self.customer = customer
        self.movie = movie
        self.number_of_tickets = number_of_tickets
    def book_ticket(self):
        print("Booking Successful!")
    def calculate_amount(self):
        return self.movie.ticket_price * self.number_of_tickets
    def generate_receipt(self):
        print("=" * 50)
        print("           MOVIE BOOKING RECEIPT")
        print("=" * 50)
        print()
        print("Customer Name   :", self.customer.customer_name)
        print("Movie Name      :", self.movie.movie_name)
        print()
        print("Ticket Price    : ₹{}".format(self.movie.ticket_price))
        print("Tickets Booked  :", self.number_of_tickets)
        print()
        print("-" * 50)
        print()
        print("Total Amount    : ₹{}".format(self.calculate_amount()))
        print()
        print("Booking Status  : CONFIRMED")
        print()
        print("=" * 50)
customer = Customer("Guddi")
movie = Movie("Avengers", 200)
booking = Booking(customer, movie, 4)
booking.book_ticket()
booking.generate_receipt()