class StudentDatabase:
    student_list = []

    @classmethod
    def add_student(cls, student):
        cls.student_list.append(student)

class Student:
    def __init__(self, student_id, name, department, is_enrolled):
        self.student_id = student_id
        self.name = name
        self.department = department
        self.is_enrolled = is_enrolled
        StudentDatabase.add_student(self)

    def enroll_student(self):
        if self.is_enrolled == False:
            self.is_enrolled = True

    def drop_student(self):
        self.is_enrolled = False

    def view_student_info(self):
        print("Student ID:", self.student_id)
        print("Name:", self.name)
        print("Department:", self.department)

        if self.is_enrolled == True:
            print("Enrollment Status: Enrolled")
        else:
            print("Enrollment Status: Not Enrolled")

s1 = Student(1, "Rakib", "EEE", True)
s2 = Student(2, "Sakib", "BBA", False)

s1.view_student_info()
print()
s2.view_student_info()

s2.enroll_student()
print()
s2.view_student_info()