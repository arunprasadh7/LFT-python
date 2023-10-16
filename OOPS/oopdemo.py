# 1 oopdemo

# from user import User, Student, Faculty, Tempfaculty
from user import *  # imports entire user class
# import user as u

# u1 = User('Arun', '123')

# print(u1.username)
# print(u1.password)

# u1.register()
# u1.login()

# # creating second object
# u2 = User('Arc', '456')

# print(u2.username)
# print(u2.password)
# u2.register()
# u2.login()

# #class variables
# print(User.users)
# u1.users = 5
# print(u1.users)


# # inheritance
# # student class
# s1 = Student()
# s1.greet_student()
# s1.register()
# s1.login()

# # faculty class
# f1 = Faculty()
# f1.greet_faculty()
# f1.register()
# f1.login()

# # multilevel inheritance
# # temp faculty class
# t1 = Tempfaculty()
# t1.greetTempFaculty()
# t1.greet_faculty()
# t1.register()
# t1.login()

# # multiple inheritance
# # studentfaculty class that inherits both student and faculty class
# print('\nMultiple Inheritance:')
# sf1 = StudentFaculty()
# sf1.register()
# sf1.login()
# sf1.greet_student()
# sf1.greet_faculty()

# #method overiding
# #creating a method greet in user class and overiding it in student subclass
# print('\nMethod overiding')
# u1 = User()
# u1.greet()

# s1.greet()

# #method chaining - joining multiple method in single statement
# #the prior function must return self inorder to chain or else error will be thrown
# print('\nMethod Chaining:')
# u2 = User()
# u2.register()
# u2.login()
# #the above code can be simplified as
# print('Chained code:')
# u2.login().register() #calling two methods in single statement(method chaining).login returns self


# #Super function
# print('\nSuper function:')
# sup1 = Student('Prasadh','99433','python', '30k')
# print(sup1.username)
# print(sup1.password)
# print(sup1.course)
# print(sup1.fee)
# sup1.greet_student()

# sup2 = Student('Storm', 'ttyl','Java','50k')
# print(sup2.username)
# print(sup2.password)
# print(sup2.course)
# print(sup2.fee)
# sup2.greet_student()

# print()
# sf1 = StudentFaculty('Invoker','tips','Blockchain','100k')
# sf1.greet()


