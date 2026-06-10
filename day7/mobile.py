class Mobile:
    def __init__(self,brand,color,price):
        self.brand=brand
        self.color=color
        self.price=price
        print("-------------------------")
def showMobileDetails(self):
        print(f"brand={self.brand}")
        print(f"color={self.color}")
        print(f"price={self.price}")
M1=Mobile("Redmi","Black",15000)
showMobileDetails(M1)
M2=Mobile("Realme","Blue",20000)
showMobileDetails(M2)
M3=Mobile("Samsung","White",30000)
showMobileDetails(M3)
M4=Mobile("Apple","Grey",50000)
showMobileDetails(M4)
M5=Mobile("OnePlus","Green",40000)
showMobileDetails(M5)        
