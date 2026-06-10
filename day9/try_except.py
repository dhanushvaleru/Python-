pin=input("enter a pin: ")
try:
    if(pin=='1234'):
        print("Login successful")
    else:
        raise TypeError("Invalid pin")
except TypeError as e:  
        print(e)