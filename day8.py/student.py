class Student:
    def __init__(self, student_id, student_name, attendance):
        self.student_id = student_id
        self.student_name = student_name
        self.attendance = attendance
class Assessment:
    def __init__(self, assessment_score):
        self.assessment_score = assessment_score
class PlacementManager:
    def __init__(self, student, assessment):
        self.student = student
        self.assessment = assessment
    def check_eligibility(self):
        return (self.student.attendance >= 75 and self.assessment.assessment_score >= 60)
    def generate_report(self):
        status = "ELIGIBLE" if self.check_eligibility() else "NOT ELIGIBLE"
        print("=" * 50)
        print("          PLACEMENT ELIGIBILITY REPORT")
        print("=" * 50)
        print()
        print(f"Student ID       : {self.student.student_id}")
        print(f"Student Name     : {self.student.student_name}")
        print()
        print(f"Attendance       : {self.student.attendance}%")
        print(f"Assessment Score : {self.assessment.assessment_score}")
        print()
        print(f"Placement Status : {status}")
        print()
        print("=" * 50)
student_id = input().strip()
student_name = input().strip()
attendance = int(input())
assessment_score = int(input())
student = Student(student_id, student_name, attendance)
assessment = Assessment(assessment_score)
manager = PlacementManager(student, assessment)
manager.generate_report()