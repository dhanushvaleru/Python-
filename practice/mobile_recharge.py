class Customer:
    def __init__(self, name, mobile):
        self.name = name
        self.mobile = mobile


class Recharge:
    def __init__(self, customer, plan, amount):
        self.customer = customer
        self.plan = plan
        self.amount = amount

    def generate_receipt(self):
        print("=" * 50)
        print("             RECHARGE RECEIPT")
        print("=" * 50)
        print()
        print("Customer Name :", self.customer.name)
        print()
        print("Plan Selected :", self.plan)
        print()
        print("Amount Paid   : ₹{}".format(self.amount))
        print()
        print("Status        : SUCCESSFUL")
        print()
        print("=" * 50)


customer = Customer("Dhanu", "9876543210")
recharge = Recharge(customer, "Unlimited 84 Days", 799)
recharge.generate_receipt()