def input_num_students():
    num_students = int(input("Enter number of students in the class: "))
    return num_students

def input_student_info():
    students = []
    for i in range(num_students):
        student_info = {}
        student_info["id"] = input("Enter student ID: ")
        student_info["name"] = input("Enter student name: ")
        student_info["dob"] = input("Enter student date of birth (DOB): ")
        students.append(student_info)
    return students

def input_num_courses():
    num_courses = int(input("Enter number of courses: "))
    return num_courses

def input_course_info():
    courses = []
    for i in range(num_courses):
        course_info = {}
        course_info["id"] = input("Enter course ID: ")
        course_info["name"] = input("Enter course name: ")
        courses.append(course_info)
    return courses

def select_course(courses):
    course_id = input("Enter course ID: ")
    if course_id not in [course["id"] for course in courses]:
        print("Invalid course ID.")
        return None
    return course_id

def input_marks(course_id, students):
    marks = {}
    for student in students:
        mark = int(input("Enter mark for student " + student["name"] + ": "))
        marks[student["id"]] = mark
    return {course_id: marks}

def list_courses(courses):
    print("Courses:")
    for course in courses:
        print(course["id"], course["name"])

def list_students(students):
    print("Students:")
    for student in students:
        print(student["id"], student["name"], student["dob"])


# Main program starts here
num_students = input_num_students()
students = input_student_info()
num_courses = input_num_courses()
courses = input_course_info()
list_courses(courses)
course_id = select_course(courses)
while course_id is None:
    course_id = select_course(courses)
marks = input_marks(course_id, students)
list_students(students)
show_marks(course_id, marks, students)
input_num_students()
input_num_courses()
