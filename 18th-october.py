#Python Inheritance

# Python Inheritance • Inheritance is an important aspect of the object-oriented paradigm. Inheritance provides code reusability to the program because we can use an existing class to create a new class instead of creating it from scratch.
# Syntax :
# class derived-class(base class):
#      <class-suite> Syntax :: 
     
# class derive-class(<base class 1>, <base class 2>, <class - suite> <base class n>):

# class vehical: #parent class
#     speed=50
#     def __init__(self,mk,md):
#         self.make=mk
#         self.model=md

#     def DisplayDetails(self):
#         print('Make :', self.make,"\nModel :",self.model)


# class swift(vehical): #child class or derived class
#     speed=100
#     def __init__(self,a,b):
#         # self.make='Hundai'
#         # self.model='V2'
#         super().__init__(a,b) #usede to access parent class
#         # pass
#     def speed_details(self):
#         print('Speed :', self.speed)
# o2=swift("Hundai","Desire")
# o2.DisplayDetails()
# o2.speed_details()

# # Hierarchical----

# class student:
#     def setPersonal(self):
#         self.roll=input("Enter the roll no : ")
#         self.name=input("Enter the name: ")
#     def getPersonal(self):
#         print("Roll:", self.roll, "\nName:", self.name,end="\t")

# class fy(student):
#     def getmarks (self):
#         self.s1=int(input("Enter subject marks: "))
#         self.s2=int(input("Enter subject marks: "))
#         self.s3=int(input("Enter subject marks: "))
#     def showmarks(self):
#         self.total=(self.s1 + self.s2 + self.s3)
#         print("Total:", self.total)
# class sy(student):
#     def getmarks(self):
#         self.s1=int(input("Enter subject marks: "))
#         self.s2=int(input("Enter subject marks: "))
#         self.s3=int(input("Enter subject marks: "))
#         self.s4=int(input("Enter subject marks: "))

#     def showmarks(self):
#         self.total=(self.s1+self.s2+self.s3+self.s4)
#         print("Total: ", self.total)


# fy_std1=fy() #First year students
# sy_std1=sy() #Second year students
# print("First year Student")
# fy_std1.setPersonal()
# fy_std1.getmarks()

# print("Second year Student")
# sy_std1.setPersonal()
# sy_std1.getmarks()

# print("Students Details")

# fy_std1.getPersonal()
# fy_std1.showmarks()
# sy_std1.getPersonal()
# sy_std1.showmarks()

# -----


#----- for bank custmer create base class for saving and loan account and create a multiple inheritance ----


# Python Multiple inheritance
# Python provides us the flexibility to inherit multiple base classes in the child class.
# Syntax :

# class Base1:
#     <class-suite>
# class Base2:
#     <class-sulte>

# class BaseN:
#     <class-suite>
# class Derived(Base1, Base2,...... BaseN):
#     <class-suite>





# Method Overriding
# • We can provide some specific implementation of the parent class method in our child class.

# Example:

# class Animal:
#     def speak(self):
#         print("speaking")
# class Dog(Animal):
#     def speak(self):
#         print("Barking")
# d = Dog()
# d.speak()

# class Distance:
#     def __init__(self,n): 
#         self.n=n

#     def __add__(self,d2): 
#         result=self.n+d2.n
#         return result

#     def __sub__(self,d2): 
#         result=self.n-d2.n
#         return result

#     def __lt__(self,d2):
#         result=self.n<d2.n
#         return result

# d1=Distance(10)
# d2=Distance(45)
# print(d1+d2)
# print(d1-d2)
# print(d1<d2)


# build a class complex having attributes real and imaginary. and perform complex number addition and subtraction opration

class Complex:
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __add__(self, other):
        return Complex(self.real + other.real, self.imaginary + other.imaginary)

    def __sub__(self, other):
        return Complex(self.real - other.real, self.imaginary - other.imaginary)

    def __str__(self):
        return f"{self.real} + {self.imaginary}i"

c1 = Complex(3, 4)  # 3 + 4i
c2 = Complex(1, 2)  # 1 + 2i

# Addition
c3 = c1 + c2
print("Addition:", c3)  # 4 + 6i

# Subtraction
c4 = c1 - c2
print("Subtraction:", c4)  # 2 + 2i
