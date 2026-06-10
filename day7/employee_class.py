class Employee():
    def __init__(self,emp_id,emp_name,emp_salary,emp_department,emp_job):
        print("Employee object is created...!")
        self.emp_id=emp_id
        self.emp_name=emp_name
        self.emp_salary=emp_salary
        self.emp_department=emp_department
        self.emp_job=emp_job
def showEmployeeDetails(self):
        print("------------------")
        print(f"emp_id={self.emp_id}")
        print(f"emp_name={self.emp_name}")
        print(f"emp_salary={self.emp_salary}")
        print(f"emp_department={self.emp_department}")
        print(f"emp_job={self.emp_job}")
emp1=Employee(101,"Dhanu",50000,"IT","Software Engineer")
showEmployeeDetails(emp1)
emp2=Employee(102,"Ravi",40000,"HR","HR Manager")
showEmployeeDetails(emp2)
emp3=Employee(103,"Raju",30000,"Sales","Sales Executive")
showEmployeeDetails(emp3) 
emp4=Employee(104,"Ramu",20000,"Marketing","Marketing Executive")
showEmployeeDetails(emp4)       
        