# # what is oops?
# import time

# class student:
#     #Attribute (data)
#     roll=0
#     sname=''
#     #Methods 

#     def setdata(self):
#         self.roll=int(input("Enter your roll no : "))
#         self.sname=input("Enter your name : ")
    
#     def getdata(self):
#         print('Roll No :',self.roll)
#         print('Name    :',self.sname)

# s1=student() #object created
# s2=student()
# s1.setdata()
# s1.getdata()
# s2.setdata()
# s2.getdata()

# print('\t Student Details')
# print("="*50)
# s1.getdata()
# s2.getdata()



# class studentmarks:
#     #Attribute (data)
#     marks=0
#     sname=''
#     is_pass=False
#     #Methods 
#     def setdata(self):
#         self.marks=int(input("Enter your marks : "))
#         self.sname=input("Enter your name : ")
#         if self.marks>=35 and self.marks<=100:
#             self.is_pass=True
        
    
#     def getdata(self):
#         print('Roll No :',self.marks)
#         print('Name    :',self.sname)
#         print("PASS!" if self.is_pass else "FAIL!")

# s1=studentmarks()
# s1.setdata()
# s1.getdata()


# Syntax::

# A constructor always has a name init and the name init is prefixed and suffixed with a double underscore().
#  We declare a constructor using def keyword,
# just like methods.

# def_init__(self):
    # #body of the constructor



# class sample:
#     c=0 #class variable
#     c=+1
#     test=0
#     def __init__(self): #constructor
#         self.n=10 # self is instence
#         # self.p=input("name") #instence var
#         self.c+=1
#         test+=1


#     def display(self):
#         print("number",self.n)
#         print(self.c)

#     def __del__(self): #distrouctor
#         print("Object destroyed")

# obj1=sample() # constructer being called automatically dont have to call to setdata(see above)
# obj1.display()
# obj2=sample()
# obj2.display()
# del(obj1) # destroy / delete the object

# common var in a class(not in menthod) is called class variable
# the var which is deefine in methid is called intence var 
# class var can be accessible by using class name


#Python program to show that the variables with a value #assigned in class declaration, are class variables



# class CSStudent:
#     stream = 'IT'
#     #Class Variable
#     def __init__(self, name, roll):
#         self.name = name

# #Instance Variable
#         self.roll = roll

# #Instance Variable

# #Objects of CSStudent class

# a = CSStudent('ABC', 1)

# b = CSStudent('DEF', 2)

# print("Student 1")

# print(a.stream)

# # prints "IT"

# print(a.roll) 
# print(a.name)

# # prints "1"

# print("Student 2")

# # prints "ABC"

# print(b.stream)

# # prints "IT"

# print(b.roll)

# # prints "2"

# print(b.name)

# # prints "DEF"

# # Class variables can be accessed using class

# #name also

# class Constr_types:
#     '''
#     def __init__(self):
#         print('Default Constructor')
#     '''
#     # we cant use both in default 
#     def __init__(Self,arg1):
#         data=arg1
#         print("Parametrised Constructor", data)

# obj1=Constr_types()
# obh2=Constr_types(10)

# SN Function

# Description

# 1 getattr(obj,name,default): It is used to access the attribute of the object.

# 2 setattr(obj, name, value): It is used to set a particular value to the specific attribute of an object.

# 3 delattr(obj, name): It is used to delete a specific attribute.

# 4 hasattr(obj, name): It returns true if the object contains some specific attribute.
# print(student.__dict__)
# print(student.__name__)
# print(student.__module__)
# print(student.__doc__)


# create a class to store a details of 5 student & display it(use array or list)

class Student:
    def __init__(self, name, roll_no, age, grade, email):
        self.name = name
        self.roll_no = roll_no
        self.age = age
        self.grade = grade
        self.email = email

    def display_details(self):
        print(f"Name: {self.name}")
        print(f"Roll No: {self.roll_no}")
        print(f"Age: {self.age}")
        print(f"Grade: {self.grade}")
        print(f"Email: {self.email}")
        print("-" * 20)


students = []


for i in range(5):
    print(f"Enter details for Student {i + 1}:")
    name = input("Enter name: ")
    roll_no = input("Enter roll number: ")
    age = int(input("Enter age: "))
    grade = input("Enter grade: ")
    email = input("Enter email: ")
    

    student = Student(name, roll_no, age, grade, email)
    students.append(student)


print("\nDisplaying Student Details:\n")
for student in students:
    student.display_details()
