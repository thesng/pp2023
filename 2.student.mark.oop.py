class Student:
    def __init__(self, id, name, dob):
        self.id = id
        self.name = name
        self.dob = dob

class Course:
    def __init__(self, id, name):
        self.id = id
        self.name = name

class Mark:
    def __init__(self, student, course, mark):
        self.student = student
        self.course = course
        self.mark = mark

def input_num_students():
    num_students = int(input("Enter number of students in the class: "))
    return num_students

def input_student_info():
    students = []
    for i in range(num_students):
        id = input("Enter student ID: ")
        name = input("Enter student name: ")
        dob = input("Enter student date of birth (DOB): ")
        student = Student(id, name, dob)
        students.append(student)
    return students

def input_num_courses():
    num_courses = int(input("Enter number of courses: "))
    return num_courses

def input_course_info():
    courses = []
    for i in range(num_courses):
        id = input("Enter course ID: ")
        name = input("Enter course name: ")
        course = Course(id, name)
        courses.append(course)
    return courses

def select_course(courses):
    course_id = input("Enter course ID: ")
    for course in courses:
        if course.id == course_id:
            return course
    print("Invalid course ID.")
    return None

def input_marks(course, students):
    marks = []
    for student in students:
        mark = int(input("Enter mark for student " + student.name + ": "))
        mark = Mark(student, course, mark)
        marks.append(mark)
    return marks

def list_courses(courses):
    print("Courses:")
    for course in courses:
        print(course.id, course.name)

def list_students(students):
    print("Students:")
    for student in students:
        print(student.id, student.name, student.dob)


# Main program starts here
num_students = input_num_students()
students = input_student_info()
num_courses = input_num_courses()
courses = input_course_info()
list_courses(courses)
course = select_course(courses)
while course is None:
    course = select_course(courses)
marks = input_marks(course, students)
list_students(students)
show_marks(course, marks, students)
