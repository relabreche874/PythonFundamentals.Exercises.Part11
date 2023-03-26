from enum import Enum
import uuid
class AliveStatus(Enum):
    deceased = 0
    alive = 1

class Person:
    def __init__(self, firstname, lastname, dob, alive):
        self.firstname = firstname
        self.lastname = lastname
        self.dob = dob
        self.alive = alive

    def update_first_name(self, firstname):
        self.firstname = firstname

    def update_last_name(self, lastname):
        self.lastname = lastname

    def update_dob(self, dob):
        self.dob = dob

    def update_status(self, status):
        self.status = status

class Instructor(Person):
    def __init__(self, firstname, lastname, dob, alive, instructor_id):  # fname, lname, dob, alive, instructor_id
        self.firstname = firstname
        self.lastname = lastname
        self.dob = dob
        self.alive = alive
        # super(Person).__init__(firstname, lastname, dob, alive)  # (fname, lname, dob, alive)
        self.instructor_id = f"Instructor_{instructor_id}" + str(uuid.uuid4())

class Student(Person):
    def __init__(self, firstname, lastname, dob, alive, student_id): #fname, lname, dob, alive, student_id
        super(Person).__init__(firstname, lastname, dob, alive)  # (fname, lname, dob, alive)
        self.student_id = f"Instructor_{student_id}" + str(uuid.uuid4())

class ZipCodeStudent(Person):
    pass

class CollegeStudent(Person):
    pass

class Classroom:

    def __init__(self):

        self.instructors = []
        self.students = []

    def add_instructor(self, instructor):
        self.instructors.append(instructor)

    def remove_instructor(self, instructor):
       self.instructors.remove(instructor)

    def add_student(self, student):
       self.students.append(student)

    def remove_student(self, student):
        self.students.append(student)

    def print_instructors(self):
        print(self.instructors)

    def print_students(self):
        print(self.students)