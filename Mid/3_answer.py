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

s1 = Student(1, "Amena", "CSE", True)
s2 = Student(2, "Rakib", "EEE", False)
s3 = Student(3, "Sakib", "BBA", True)

for s in StudentDatabase.student_list:
    print(s.student_id, s.name, s.department, s.is_enrolled)