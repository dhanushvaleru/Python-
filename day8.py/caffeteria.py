class Employee:
    def __init__(self, employee_id, employee_name):
        self.employee_id = employee_id
        self.employee_name = employee_name
class FoodItem:
    def __init__(self, item_name, price):
        self.item_name = item_name
        self.price = price
class Order:
    def __init__(self, order_id):
        self.order_id = order_id
        self.ordered_items = []
    def add_item(self, item):
        self.ordered_items.append(item)
    def calculate_total(self):
        return sum(item.price for item in self.ordered_items)
    def generate_bill(self, employee):
        print("=" * 50)
        print("            CORPORATE CAFETERIA BILL")
        print("=" * 50)
        print()
        print(f"Employee ID     : {employee.employee_id}")
        print(f"Employee Name   : {employee.employee_name}")
        print()
        print("-" * 50)
        print(f"{'Item':<28}Price")
        print("-" * 50)
        for item in self.ordered_items:
            print(f"{item.item_name:<28}${item.price}")
        print("-" * 50)
        print()
        print(f"{'Total Amount':<28}${self.calculate_total()}")
        print()
        print(f"{'Payment Status':<28}PAID")
        print()
        print("=" * 50)
class Cafeteria:
    def __init__(self):
        self.menu = []
    def add_food_item(self, item):
        self.menu.append(item)
    def display_menu(self):
        for item in self.menu:
            print(f"{item.item_name} {item.price}")
employee = Employee("E101", "Ryan")
cafeteria = Cafeteria()
cafeteria.add_food_item(FoodItem('Coffee', 40))
cafeteria.add_food_item(FoodItem('Sandwich', 80))
cafeteria.add_food_item(FoodItem('Brownie', 60))
order = Order("O101")
order.add_item(cafeteria.menu[0])  
order.add_item(cafeteria.menu[1])  
order.add_item(cafeteria.menu[2])  
order.generate_bill(employee)