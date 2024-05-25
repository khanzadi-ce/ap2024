# Author: P. Khanzadi
# Python: 3.9.7

class Student:
    def __init__(self, first_name, last_name, student_id):
        self.f_name = first_name 
        self.l_name = last_name 
        self.s_id   = student_id
        self.registered_courses = []

    def add_course(self,course_id:int) -> bool:
        if self.register_rule_max_courses(max_number_of_course=3, registered_courses = self.registered_courses) == True:
            self.registered_courses.append(course_id)
            return True
        else: 
            print('Error in following registration rule: maximum number of courses')
            return False


    def register_rule_max_courses(self,max_number_of_course:int,registered_courses:list) -> bool:
        
        # check maximum number of course is defiend or not 
        if max_number_of_course is None:
            self.max_number_of_course = 3
        else: 
            self.max_number_of_course = max_number_of_course
    
        # rule 1
        if len(registered_courses) >= max_number_of_course:
            return False
        else:
            return True
        
