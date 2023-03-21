import math
import numpy as np
import curses

class Student:
    def __init__(self, id, name, dob):
        self.id = id
        self.name = name
        self.dob = dob

class Course:
    def __init__(self, id, name, credits):
        self.id = id
        self.name = name
        self.credits = credits

class Mark:
    def __init__(self, student, course, mark):
        self.student = student
        self.course = course
        self.mark = mark

def input_num_students():
    num_students = int(input("Enter number of students in the class: "))
    return num_students

def input_student_info(num_students):
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

def input_course_info(num_courses):
    courses = []
    for i in range(num_courses):
        id = input("Enter course ID: ")
        name = input("Enter course name: ")
        credits = int(input("Enter course credits: "))
        course = Course(id, name, credits)
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
        mark = math.floor(mark * 10) / 10
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

def calculate_gpa(student, marks):
    total_credits = 0
    weighted_sum = 0
    for mark in marks:
        if mark.student == student:
            total_credits += mark.course.credits
            weighted_sum += mark.course.credits * mark.mark
    if total_credits == 0:
        return 0
    return weighted_sum / total_credits

def sort_students_by_gpa(students, marks):
    students_with_gpa = [(student, calculate_gpa(student, marks)) for student in students]
    students_with_gpa.sort(key=lambda x: x[1], reverse=True)
    return students_with_gpa

# Main program starts here
num_students = input_num_students()
students = input_student_info(num_students)
num_courses = input_num_courses()
courses = input_course_info(num_courses)
list_courses(courses)
course = select_course(courses)
while course is None:
    course = select_course(courses)
marks = input_marks(course, students)
list_students(students)
sorted_students = sort_students_by_gpa(students, marks)
for student, gpa in sorted_students:
    print(student.name + "'s GPA: " + str(gpa))