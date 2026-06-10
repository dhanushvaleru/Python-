balance=5000
try:
    amount=int(input("Enter the amount to withdraw: "))
    if amount > balance:
        raise ValueError("Insufficient funds")
    balance -= amount
    print("Withdrawal successful")
except ValueError as e:
    print("Transaction failed:", e)