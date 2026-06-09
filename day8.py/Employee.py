class Employee:
    def work_hours(self):
        print("Employee is working 8 hours a day...")
class Intern(Employee):
    def work_hours(self):
        print("Intern is working 4 hours a day...")   
intern1=Intern()
intern1.work_hours()             