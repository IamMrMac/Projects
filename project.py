"""
Create a parent class (Person). The Student and Instructor class receive inheritance from this parent class
The parent class has the Name and Id_number attributes
"""

class Person:
    def __init__(self, name, id_number) -> None:
        self.name = name
        self.id_number = id_number
        
    # Create a __str__ method to return a string representation of the person
    def __str__(self):
        return f"Name: {self.name}, ID: {self.id_number}"


""" 
Create a Student class that inherits from the Parent class (Person). The student class inherits Name
and Id_number from the parent class (Person), it also has attribute Major for the student's major
"""

class Student(Person):
    def __init__(self, name, id_number, major) -> None:
        super().__init__(name, id_number)
        self.major = major
        
    # Create an override of the __str__ method to include the student's major.                      
    def __str__(self):
        return f"Name: {self.name}, ID: {self.id_number}, Major: {self.major}"
    
  
""" 
Create a Instructor class that inherits from the Parent class (Person). The Instructor class inherits Name
and Id_number from the parent class (Person), it also has attribute Department for the student's department
"""    
  
class Instructor(Person):
    def __init__(self, name, id_number, department) -> None:
        super().__init__(name, id_number)
        self.department = department 
        
    # Create an override of the __str__ method to include the Instructors department.  
    def __str__(self):
        return f"Name: {self.name}, ID: {self.id_number}, Department: {self.department}"


""" 
Create a Course class tWith the following attributes
1. Course_name
2. course_id
3. enrolled_students
""" 

class Course:
    def __init__(self, course_name, course_id) -> None:
        self.course_name = course_name
        self.course_id = course_id
        self.enrolled_students = []
    
    #  Create a Method to add students to the course  
    def add_student(self, student):
        self.enrolled_students.append(student)
    
     #  Create a Method to remove students from the course    
    def remove_student(self, student):
        self.enrolled_students.remove(student)
    
     # Create an override of the __str__ method to return a string representation of the course.
    def __str__(self):
        enrolled_students_str = ', '.join([student.name for student in self.enrolled_students])
        return f"Course Name: {self.course_name}, Course Id: {self.course_id}, Enrolled_students: [{enrolled_students_str}]"

    
 
"""
Create an Enrollment class with the following attributes
1. student
2. course
3. grade:
"""   
class Enrollment:
    def __init__(self, student, course) -> None:
        self.student = student
        self.course = course 
        self.grade = None 
    
     #  Create a Method to assign a grade to the student.    
    def grade_assigned(self, grade):
        self.grade = grade 
    
    #  # Create an override of the __str__ method to return a string representation of the enrollment.    
    def __str__(self):
        return f"Student: {self.student}, Course: {self.course}, Grade: {self.grade}"
  
  
  
"""
Create a Student Management System
"""
class Student_Management_System:
    def __init__(self) -> None:
            self.students = []
            self.instructors = []
            self.courses = []
            self.enrollments = []
            
    # Create a method to Add students        
    def add_student(self, student):
        # Check if the student already exists
        for existing_student in self.students:
            if existing_student.id_number == student.id_number:
                return f"Student with ID {student.id_number} already exists."        
        # If the student does not exist, add them to the list
        else:
            self.students.append(student)
            return f"Student with ID {student.id_number} has been added."
    
    #  Create a method to remove students
    def remove_student(self, student_to_remove):
        # Check if the student already exists and remove
        for student in self.students:
            if student.id_number == student_to_remove.id_number:
                self.students.remove(student)
                return f"Student with ID {student_to_remove.id_number} has been removed."
        return f"Student not found."
    
    # Create a method to update students list
    def update_students(self):
        return self.students
    
    # Create a method to Add instructor
    def add_instructor(self, instructor):
        # Check if the instructor already exists
        for existing_instructor in self.instructors:
            if existing_instructor.id_number == instructor.id_number:
                return f"Instructor with ID {instructor.id_number} already exists."        
        # If the instructor does not exist, add them to the list
        self.instructors.append(instructor)
        return f"Instructor with ID {instructor.id_number} has been added."
    
    # Create a method to Remove instructor        
    def remove_instructor(self, instructor_to_remove):
        # Check if the instructor already exists and remove
        for instructor in self.instructors:
            if instructor.id_number == instructor_to_remove.id_number:
                self.instructors.remove(instructor)
                return f"student with ID {instructor_to_remove.id_number} has been removed"
        return f"Student not found" 
    
    # Create a method to update Instructor list
    def update_instructors(self):
        return self.instructors       
    
    # Create a method to Add Courses
    def add_course(self, course):
        # Check if the course already exists
        for existing_course in self.courses:
            if existing_course.course_id == course.course_id:
                return f"Course with ID {course.course_id} already exists."
        # If the course does not exist, add it to the list
        self.courses.append(course)
        return f"Course with ID {course.course_id} has been added."
          
    # Create a method to Remove Courses
    def remove_course(self, course_to_remove):
        for course in self.courses:
            if course.course_id == course_to_remove.course_id:
                self.courses.remove(course)
                return f"Course with ID {course_to_remove.course_id} has been removed."
        return f"Course not found."

    # Create a method to update Course list
    def update_courses(self):
        return self.courses
    
    # Enroll students in courses
    def enroll_student(self, student, course):
        # Check if the student is already enrolled in the course
        for enrollment in self.enrollments:
            if enrollment.student.id_number == student.id_number and enrollment.course.course_id == course.course_id:
                return f"Student {student.name} is already enrolled in course {course.course_name}"

        # If not already enrolled, proceed with enrollment
        enrollment = Enrollment(student, course)
        self.enrollments.append(enrollment)
        course.add_student(student)
        return f"Student {student.name} enrolled in course {course.course_name}"
  
    # Assign grades to students, with the course
    def assign_grade(self, student, course, grade):
        for enrollment in self.enrollments:
            if enrollment.student.id_number == student.id_number and enrollment.course.course_id == course.course_id:
                enrollment.grade_assigned(grade)
                return f"Grade {grade} assigned to student {student.name} for course {course.course_name}"
        return f"No record for student {student.name} in course {course.course_name}"
    
    # Retrieve students in a specific course
    def get_students_in_course(self, course):
        students_in_course = []
        for enrollment in self.enrollments:
             if enrollment.course.course_id == course.course_id:
                students_in_course.append(enrollment.student)
        return students_in_course
    
    # Retrieve courses for a specific Student
    def get_courses_for_student(self, student):
        # Create a dictionary mapping student IDs to lists of their courses
        student_courses = {}
        for enrollment in self.enrollments:
            student_id = enrollment.student.id_number
            if student_id not in student_courses:
                student_courses[student_id] = []
            student_courses[student_id].append(enrollment.course)
        return student_courses.get(student.id_number, [])