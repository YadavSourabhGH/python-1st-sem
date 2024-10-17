# # what is oops?
import time

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



class sample:
    def __init__(self): #constructor
        self.n=10

    def display(self):
        print("number",self.n)

    def __del__(self): #distrouctor
        print("Object destroyed")

obj1=sample() # constructer being called automatically dont have to call to setdata(see above)
obj1.display()
# del(obj1) # destroy / delete the object

