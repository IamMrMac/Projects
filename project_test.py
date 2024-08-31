# Test Example for Student Management System
from project import Person
from project import Student
from project import Instructor
from project import Course
from project import Enrollment
from project import Student_Management_System


# Test Example for Student Management System

# Create instances of Student and Instructor
student1 = Student("Samuel", "S001", "Computer Science")
student2 = Student("Mark", "S002", "Mathematics")
instructor1 = Instructor("Dr. Smith", "I001", "Physics")
instructor2 = Instructor("Dr. Johnson", "I002", "Chemistry")

# Create instances of Course
course1 = Course("Data Structures", "C001")
course2 = Course("Calculus", "C002")

# Create an instance of Student Management System
sms = Student_Management_System()

# Add students 
print(sms.add_student(student1))  
print(sms.add_student(student2))  
print()

# Add instructors
print(sms.add_instructor(instructor1))  
print(sms.add_instructor(instructor2))  
print()

# Add courses
print(sms.add_course(course1))  
print(sms.add_course(course2))  

print()
# Enroll students in courses
print(sms.enroll_student(student1, course1))  
print(sms.enroll_student(student2, course2))  

print()
# Assign grades to students
print(sms.assign_grade(student1, course1, "A"))  
print(sms.assign_grade(student2, course2, "B"))  
print()

# Retrieve list of students in a specific course
students_in_course1 = sms.get_students_in_course(course1)
print(f"Students in {course1.course_name}: {[str(student) for student in students_in_course1]}")
print()

# Retrieve list of courses a specific student is enrolled in
courses_for_student1 = sms.get_courses_for_student(student1)
print(f"Courses for {student1.name}: {[str(course) for course in courses_for_student1]}")