'''
name: Cameron Ball
FSUID: cbb18
'''
from math import log

class student:
    def __init__(self, firstname = '', lastname = '', gender = '', status = '', gpa = 0.0):
        self.firstname = firstname
        self.lastname = lastname
        
        if gender != "male" and gender != "female":
            self.gender = "male"
        else:
            self.gender = gender
        
        if status != "freshman" and status != "sophomore" and status != "junior" and status != "senior":
            self.status = "freshman"
        else:
            self.status = status
        self.gpa = gpa

    def show_myself(self):
        l = list()
        for attribute in self.__dict__:
            l.append(attribute)
        print("{", end='')
        for attribute in l[:-1]:    
            exec("print(\"\'\" + attribute + \"\': \'\" + self." + str(attribute) + "+ \"\'\", end=', '" + ")")
        exec("print(\"\'\" + l[-1] + \"\': \'\" + self." + str(l[-1]) + "+ \"\'}\")")

    def study_time(self, study_time):
        temp = float(self.gpa) + log(study_time)
        if temp > 4.0:
            self.gpa = 4.0
        else:
            self.gpa = temp


if __name__ == "__main__":
    
    student_list = [
        student("Mike", "Barnes", "male", "freshman", "4.0"),
        student("Jim", "Nickerson", "male", "sophomore", "3.0"),
        student("Jack", "Indabox", "male", "junior", "2.5"),
        student("Jane", "Miller", "female", "senior", "3.6"),
        student("Mary", "Scott", "female", "senior", "2.7")
    ]
    
    for student in student_list:
        student.show_myself()