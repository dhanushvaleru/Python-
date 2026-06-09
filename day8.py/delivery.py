class Customer:
    def delivery(self):
        print("Delivery charge: $5")
class PrimeCustomer(Customer):
    def delivery(self):
        print("Delivery charge:$2")
customer1=PrimeCustomer()
customer1.delivery()        
