class Employee:
    def __init__(self, employee_id, employee_name):
        self.employee_id = employee_id
        self.employee_name = employee_name
class FoodItem:
    def __init__(self, item_name, price):
        self.item_name = item_name
        self.price = price
class Order:
    def __init__(self):
        self.ordered_items = []  
    def add_item(self, item):
        self.ordered_items.append(item)     
    def bill(self,emp):
        total = sum(i.price for i in self.ordered_items)
        print("=" * 50)
        print(f"Employee ID     : {emp.employee_id}")
        print(f"Employee Name   : {emp.employee_name}")
        print("-" * 50)
        print("Item\t\tPrice")
        print("-" * 50)
        for item in self.ordered_items:
            print(f"{item.item_name}\t\t{item.price}")
        print("-" * 50)             
        print(f"Total Amount\t{total}")
        print(f"Payment Status\tPAID")      
class Cafeteria:
    def __init__(self):
        self.menu = []
    def add_food_item(self, item):
        self.menu.append(item)  
employee = Employee("E101", "Ryan") 
cafeteria = Cafeteria() 
cafeteria.add_food_item(FoodItem('Coffee', 40))
cafeteria.add_food_item(FoodItem('Sandwich', 80))
cafeteria.add_food_item(FoodItem('Brownie', 60))
order = Order() 
order.add_item(cafeteria.menu[0])   
order.add_item(cafeteria.menu[1])   
order.add_item(cafeteria.menu[2])   
order.bill(employee)
