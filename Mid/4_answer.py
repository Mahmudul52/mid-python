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

s1 = Student(1, "Sakib", "CSE", False)

print(s1.is_enrolled)  
s1.enroll_student()
print(s1.is_enrolled)  