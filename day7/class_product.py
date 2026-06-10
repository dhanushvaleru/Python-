class Product:
    def __init__(self, name, price):
        print("Product object is created...!")
        self.name = name
        self.price = price
        print("------------------")
P1=Product("Phone",20000)
print(f"name={P1.name}")
print(f"price={P1.price}")
P2=Product("lap",50000)
print(f"name={P2.name}") 
print(f"price={P2.price}")
P3=Product("AC",20000)
print(f"name={P3.name}")
print(f"price={P3.price}")       

    