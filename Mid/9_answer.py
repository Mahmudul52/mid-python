class StudentDatabase:
    student_list = []

    @classmethod
    def add_student(cls, student):
        cls.student_list.append(student)

    @classmethod
    def find_student(cls, student_id):
        for s in cls.student_list:
            if s.student_id == student_id:
                return s
        raise ValueError("Invalid student ID")

    @classmethod
    def enroll_by_id(cls, student_id):
        student = cls.find_student(student_id)
        student.enroll_student()

    @classmethod
    def drop_by_id(cls, student_id):
        student = cls.find_student(student_id)
        student.drop_student()

class Student:
    def __init__(self, student_id, name, department, is_enrolled):
        self.__student_id = student_id
        self.__name = name
        self.__department = department
        self.__is_enrolled = is_enrolled
        StudentDatabase.add_student(self)

    @property
    def student_id(self):
        return self.__student_id

    def enroll_student(self):
        if self.__is_enrolled == True:
            raise ValueError("Student is already enrolled")
        self.__is_enrolled = True

    def drop_student(self):
        if self.__is_enrolled == False:
            raise ValueError("Student is not enrolled")
        self.__is_enrolled = False

    def view_student_info(self):
        print("Student ID:", self.__student_id)
        print("Name:", self.__name)
        print("Department:", self.__department)

        if self.__is_enrolled == True:
            print("Enrollment Status: Enrolled")
        else:
            print("Enrollment Status: Not Enrolled")

s1 = Student(1, "Rakib", "EEE", True)
s2 = Student(2, "Sakib", "BBA", False)

s1.view_student_info()

try:
    print(s1.name)
except AttributeError:
    print("Error: name is private")

try:
    print(s1.__is_enrolled)
except AttributeError:
    print("Error: is_enrolled is private")

s2.enroll_student()
s2.view_student_info()