# Author: P. Khanzadi
# Python: 3.9.7

# Library
from classes.student import Student
from classes.course import Course


# Define courses (instance from Course class) 
course_mathematics = Course('mathematics',112)
course_physics     = Course('physics',213)
course_fm          = Course('formal methods',712)
course_data_mining = Course('Data Mining',512)

# Create students (instance from Student class) 
student_1 = Student('Pouria','Khanzadi','157123456')

# Add course: 1
student_1.add_course(course_id = course_mathematics.course_id)

# Add course: 2
student_1.add_course(course_id = course_physics.course_id)

# Add course: 3
student_1.add_course(course_id = course_fm.course_id)

# Add course: 4
student_1.add_course(course_id = course_data_mining.course_id)
