# user.py

class User():

    # users = 0	#class variable

    # def __init__(self, username, password):
    # 	self.username = username
    # 	self.password = password	#instance variables/instance attributes
    # 	User.users += 1

    def register(self):
        print(f'Registering .')

    def login(self):
        print(f'Logging in .')

    def greet(self):
     	print('Hello user.This is a user class method.')


# Inheritance

# creating a student subclass
class Student(User):  # Student inherits User
    def greet_student(self):
        print('Hi student...')

    def greet(self):
    	print('Hello student. This is a student class method.')

# creaiing another subclass Faculty


class Faculty(User):
    def greet_faculty(self):
        print('Hi faculty...')


# multilevell inheritance
# creating a tempfaculty class that inherits from faculty

class Tempfaculty(Faculty):
    # tempfaculty inherits faculty which inherits user class
    # multilevel inheritance
    def greetTempFaculty(self):
        print('Hi temporary faculty.')

# multiple inheritance
# creating studentfaculty class that inherits both student & faculty class


class StudentFaculty(Student, Faculty):
    pass
