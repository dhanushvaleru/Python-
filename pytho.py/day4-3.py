#n1=int(input("Enter no of pizzas: "))
#for i in range(n1):
pizza=(input("Enter the size of pizza: "))
tot_bill=0
if(pizza=="small"):
    price=10
    n=int(input("Enter the no of toppings: "))
    for i in range(n):
     toppings=(input("Enter your Toppings: "))
    if(toppings=="cheese"):
        cheese=2
        tot_bill=price+cheese
        print(f"Total bill is: {tot_bill}$ ")
    elif(toppings=="pepperoni"):
        pepperoni=3
        tot_bill=price+pepperoni
        print(f"Total bill is: {tot_bill}$ ")
    elif(toppings=="olives"):
        olives=5
        tot_bill=price+olives
        print(f"Total bill is: {tot_bill}$ ")
    elif(toppings=="Jalapenos"):
        Jalapenos=5
        tot_bill=price+Jalapenos
        print(f"Total bill is: {tot_bill}$ ")
    else:
         print("Not Available")
elif(pizza=="medium"):
    price=15
    n=int(input("Enter the no of toppings: "))
    for i in range(n):
     toppings=(input("Enter your Toppings: "))
    if(toppings=="cheese"):
        cheese=2
        tot_bill=price+cheese
        print(f"Total bill is: {tot_bill}$ ")
    elif(toppings=="pepperoni"):
        pepperoni=3
        tot_bill=price+pepperoni
        print(f"Total bill is: {tot_bill}$ ")
    elif(toppings=="olives"):
        olives=5
        tot_bill=price+olives
        print(f"Total bill is: {tot_bill}$ ")
    elif(toppings=="Jalapenos"):
        Jalapenos=5
        tot_bill=price+Jalapenos
        print(f"Total bill is: {tot_bill}$ ")
    else:
         print("Not Available")
elif(pizza=="large"):
    price=20
    n=int(input("Enter the no of toppings: "))
    for i in range(n):
     toppings=(input("Enter your Toppings: "))
    if(toppings=="cheese"):
        cheese=2
        tot_bill=price+cheese
        print(f"Total bill is: {tot_bill}$ ")
    elif(toppings=="pepperoni"):
        pepperoni=3
        tot_bill=price+pepperoni
        print(f"Total bill is: {tot_bill}$ ")
    elif(toppings=="olives"):
        olives=5
        tot_bill=price+olives
        print(f"Total bill is: {tot_bill}$ ")
    elif(toppings=="Jalapenos"):
        Jalapenos=5
        tot_bill=price+Jalapenos
        print(f"Total bill is: {tot_bill}$ ")
    else:
         print("Not Available")
else:
    print("Error")