class Ride:
    def fare(self):
        print("Fare: ₹100")
class LuxuryRide(Ride):
    def fare(self):
        print("Fare: ₹300")
luxury = LuxuryRide()
luxury.fare()  
normal = Ride()
normal.fare()