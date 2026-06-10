print("Program Starts")
a=10
print("a=",a)
try:
    print(a/0)
except ZeroDivisionError as e:
    print("Not possible to divide with zero if u divide it gives",e)
print("Program Ends")