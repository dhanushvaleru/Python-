slots=list(map(str,input("Enter slots:").split()))
times_lots=input("Enter the requisted slots:")
print("slots already booked" if times_lots in slots else "slots are available")