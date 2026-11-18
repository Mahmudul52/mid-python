class Student:
    def __init__(self, name, roll):
        self.name = name
        self.roll = roll

class StudentDatabase:
    student_list = []

    @classmethod
    def add_student(cls, student):
        cls.student_list.append(student)

s1 = Student("Amena", 1)
s2 = Student("Rakib", 2)

StudentDatabase.add_student(s1)
StudentDatabase.add_student(s2)

print(len(StudentDatabase.student_list))

for s in StudentDatabase.student_list:
    print(s.name, s.roll)