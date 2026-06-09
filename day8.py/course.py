# Parent class
class Course:
    def course_fee(self):
        print("Course Fee: ₹5000")

# Child class
class AdvancedCourse(Course):
    def course_fee(self):
        print("Course Fee: ₹12000")

# Test Case 1: Advanced Course
advanced = AdvancedCourse()
advanced.course_fee()

# Test Case 2: Basic Course
basic = Course()
basic.course_fee()