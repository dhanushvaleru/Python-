class Student:
    def __init__(self,name,age):
        print("Student object is created...!")
        self.name=name
        self.age=age
def details(self):        
        print("------------------")
        print(f"name={self.name}")
        print(f"age={self.age}")
s1=Student("Dhanu",22)
details(s1)    
s2=Student("Ravi",21)
details(s2)
s3=Student("Raju",23)
details(s3)
s4=Student("Ramu",24)
details(s4)