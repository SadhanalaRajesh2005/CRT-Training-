# constructor example
# class Student:
#     def __init__(self):
#         print("constructor is called ")
# s1 = Student()


# not constructor uses in example
# class Student:
#     pass
# s1 = Student()
# s1.name = "rajesh"
# s1.branch = "AI"
# print(s1.name)
# print(s1.branch)

# constructor with parameters
# class Student:
#    def __init__(self,name,age):
#       self.name = name
#       self.age = age
# s1 = Student("rajesh",23)
# print(s1.name)
# print(s1.age)



# # normal method
# class Student:
#    def __init__(self):
#       print("constuctor")
#     # normal metod
#    def display(self):
#       print("normal method")
# c1 = Student()
# c1.display()
      


# class Student:
#     def __init__(self,name,marks):
#         #   instance variables
#           self.name = name
#           self.marks = marks
# s1 = Student("rajesh",45)
# s2 = Student("razak",56)
# print(s1.name)
# print(s2.marks)

# class Student:
#     def __init__(self,name,marks):
#         #   instance variables
#           self.name = name
#           self.marks = marks
#     #  instance methods
#     def display(self):
#          print(self.name)
#          print(self.marks)
# s1 = Student("rajesh",56)
# s1.display()

# dynamically
# class Student:
#     pass
# s1 = Student()
# s1.name = "rajesh"
# s1.age = 20

# print(s1.name)
# print(s1.age)



# class variables
# class Student:
#     # class variable
#     college_name = "CITY"
#     def __init__(self,branch):
#         # isinstance variables

#         self.branch = branch
#         # normal method
#     def display(self):
#         print(self.college_name)
# s1 = Student("CSE")
# print(s1.college_name)
# print(s1.branch)


# class Student:
#     def show(self):
#         print(self)
# s1 = Student()
# print(s1)
# s1.show()
      

# class methods
# class Student:
#     college = "CITY"
#     @classmethod
#     def show_college(cls):
#         print(cls.college)

# Student.show_college



# staticmethod/
# class Calculator:
#     @staticmethod
#     def add(a,b):
#         return a+b
# print(Calculator.add(10,20))
    
# task : create a class named student
#     create constructor
#     class variable
#     instance variables
#     instance method
#     classmethod
#     staticmethod

class Student:
    college = "CITY"
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def display(self):
        print(self.name)
        print(self.age)

    @classmethod
    def show_college(cls):
      print(cls.college)


    @staticmethod
    def add(a,b):
      return a+b
    print(add(10,20))
s1 = Student("rajesh",20)
s1.display()
Student.show_college()

        