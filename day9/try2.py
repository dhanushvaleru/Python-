try:
    monthly_salary=int(input("Enter your monthly salary: "))
    if monthly_salary < 0:
        raise ValueError
    annual_salary=monthly_salary*12
    print("Your annual salary is:", annual_salary)
except ValueError:
    print("Please enter a valid salary amount.")