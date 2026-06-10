class vehicle:
    def __init__(self, b,p,c,s):
        self.b=b
        self.p=p
        self.c=c
        self.s=s
        print("Vehicle class constructor")
class Bike(vehicle):
    def __init__(self, b,p,c,s,g,m):
        super().__init__(b,p,c,s)
        self.g=g
        self.m=m
        print("Bike class constructor") 
b1=Bike("Honda",100000,"Petrol","Manual","CBR",150)
