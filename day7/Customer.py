class customer:
    def _init_(self):
       pass
    def set_id(self,id):
        self.id=id
    def set_name(self,name):
        self.name=name
    def set_age(self,age):
        self.age=age
    def get_id(self):
        return self.id
    def get_name(self):
        return self.name
    def get_age(self):
        return self.age
C1=customer()
C1.set_id(101)
C1.set_name("Dhanu")        
C1.set_age(25)
print("Customer Details")
print("Customer id:",C1.get_id())   
print("Customer name:",C1.get_name())
print("Customer age:",C1.get_age())
C2=customer()
C2.set_id(102)
C2.set_name("Ravi")
C2.set_age(30)
print("Customer Details")
print("Customer id:",C2.get_id())
print("Customer name:",C2.get_name())
print("Customer age:",C2.get_age())