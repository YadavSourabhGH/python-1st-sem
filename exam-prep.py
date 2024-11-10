# # Using % operator
# name = "Alice"
# print("Hello, %s!" % name)

# # Using .format() method
# print("Hello, {}!".format(name))

# # Using f-string (Python 3.6+)
# print(f"Hello, {name}!")


# Mutable vs. Immutable Data Types:

# Mutable: Lists, dictionaries, sets – can be changed after creation.
# Immutable: Integers, floats, strings, tuples – cannot be changed after creation.


# Operators:

# Arithmetic: +, -, *, /, //, %, **
# Logical: and, or, not


# Conditional Statements:

# if, elif, else statements 



# Control Statements:

# break, continue, pass



# # Arithmetic Operators
# a = 10
# b = 3
# print("Addition:", a + b)
# print("Subtraction:", a - b)
# print("Multiplication:", a * b)
# print("Division:", a / b)
# print("Floor Division:", a // b)
# print("Modulus:", a % b)
# print("Exponentiation:", a ** b)

# # Logical Operators
# x = True
# y = False
# print("x and y:", x and y)
# print("x or y:", x or y)
# print("not x:", not x)



# # conditional statement
# num = "d"
# if num > 0:
#     print("Positive number")
# elif num == 0:
#     print("Zero")
# else:
#     print("Negative number")




# # 5. For and While Loop
# # For loop
# for i in range(5):
#     print("For Loop:", i)

# # While loop
# i = 0
# while i < 5:
#     print("While Loop:", i)
#     i += 1



# # 6. Control Statements
# for i in range(5):
#     if i == 2:
#         continue  # Skips the rest of the code below for this iteration
#     elif i == 4:
#         break  # Exits the loop
#     print("Value:", i)

# # Pass statement example
# def my_function():
#     pass  # Does nothing, a placeholder



# # 7 define a function

# def greet(name,time):
#     print(f"Hello {name.upper()}\nGood {time}")

# greet("sourabh","evening")

# -------

# def person_info(name, age):
#     print(f"Name: {name}, Age: {age}")

# # Positional arguments
# person_info("Alice", 25)

# # Keyword arguments
# person_info(age=25, name="Alice")


# -------
# import random

# print("Random number:", random.random())
# print("Random integer between 1 and 10:", random.randint(1, 10))
# print("Random choice from list:", random.choice([1, 2, 3, 4, 5]))
# my_list = [1, 2, 3, 4, 5]
# random.shuffle(my_list)
# print("Shuffled list:", my_list)




# # break
# for i in range(5):
#     if i == 3:
#         break
#     print("Using break:", i)

# # continue
# for i in range(5):
#     if i == 3:
#         continue
#     print("Using continue:", i)

# # pass
# for i in range(5):
#     if i == 3:
#         pass
#     print("Using pass:", i)




# def sum_numbers(*args):
#     print(args)
#     return sum(args)

# print(sum_numbers(1, 2, 3, 4))

# def print_info(**kwargs):
#     print(kwargs)
#     for key, value in kwargs.items():
#         print(f"{key}: {value}")

# print_info(name="Alice", age=25, city="New York")



# import math

# print("Ceil:", math.ceil(4.2))
# print("Trunc:", math.trunc(4.2))
# print("Floor:", math.floor(4.2))
# print("Factorial:", math.factorial(5))
# print("Absolute:", math.fabs(-4.2))
# print("Power:", math.pow(2, 3))
# print("Modulo:", math.fmod(20, 3))
# print("Sum:", math.fsum([1, 2, 3, 4]))
# print("Square root:", math.sqrt(16))
# print("Product:", math.prod([1, 2, 3, 4]))





# s = "Hello World"
# print("Lowercase:", s.lower())
# print("Uppercase:", s.upper())
# print("Title Case:", s.title())
# print("Is Upper:", s.isupper())
# print("Count 'o':", s.count('o'))


# s = "Python"
# print("Forward Indexing:", s[0])  # 'P'
# print("Backward Indexing:", s[-1])  # 'n'
# print("Slicing:", s[1:4])  # 'yth'




# # Creating a list
# my_list = [1, 2, 3, 4, 5]

# # Remove element
# my_list.remove(3)
# print("Remove by value:", my_list)

# # remove the index number element
# my_list.pop(1)
# print("Pop by index:", my_list)

# # clear the list
# my_list.clear()
# print("Cleared list:", my_list)



# squares = [x ** 2 for x in range(1, 101)]
# print(squares)




# a = {1, 2, 3}
# b = {3, 4, 5}

# print("Union:", a | b)
# print("Intersection:", a & b)
# print("Difference:", a - b)



# empty_tuple = ()
# singleton_tuple = (1,)

# # Lists are mutable, tuples are immutable
# my_list = [1, 2]
# my_tuple = (1, 2)





# import array as arr

# my_array = arr.array('i', [1, 2, 3])
# print("Array:", my_array)
# my_array.append(4)
# print("Array after append:", my_array)
# my_array[0] = 10
# print("Modified array:", my_array)



# class Person:
#     def __init__(self, name):
#         self.name=name
    
# person1 = Person("Sourabh")
# print(person1.name)




# class Example:
#     # def __init__(self):  # Default constructor
#     #     self.data = "Default data"

#     def __init__(self, data):  # Parameterized constructor
#         self.data = data


# # ex = Example()
# ex2 = Example("HI")
# print( ex2.data)




# class Sample:
#     class_variable = "Class Variable"  # Class variable

#     def __init__(self, instance_variable):
#         self.instance_variable = instance_variable

# obj = Sample("Instance Variable")
# print("Class variable:", Sample.class_variable)
# print("Instance variable:", obj.instance_variable)


# Hierarchical Inheritance
# class Parent:
#     pass

# class Child1(Parent):
#     pass

# class Child2(Parent):
#     pass



# class A:
#     pass

# class B(A):  # Single inheritance
#     pass

# class C(B):  # Multilevel inheritance
#     pass





# try:
#     x = 1 / 0
# except ZeroDivisionError:
#     print("Cannot divide by zero")
# finally:
#     print("End of program")




# # lambda function
# add = lambda x,y: x+y
# sub = lambda x,y: x-y
# multi = lambda x,y: x*y
# div = lambda x,y: x/y
# expo = lambda x,y: x**y



# print(add(3,4))
# print(sub(3,4))
# print(multi(3,4))
# print(div(3,4))
# print(expo(3,4))



# dunder (magic) method
# class Age:
#     def __init__(self,age):
#         self.age = age
    
#     def __add__(self,other):
#         print(self.age+other.age)

# ram=Age(15)
# sam=Age(10)
# ram.__add__(sam)



# # list compression
# squares = [x ** 2 for x in range(1, 11)]
# print(squares)






# practical quesion sol

# # 3) WAP to add numbers from 5 to 15 using for loop.
# addition=0
# for i in range(5,16):
#     addition+=i
# print(addition)



# # 4) WAP to find factorial of a number.
# n = int(input("Enter number to find its factorial: "))
# result=1
# for i in range(1,n+1):
#     result*=i
# print(result)



# 5) WAP to WAP to print the following patterns:
# *
# * *
# * * *
# * * * *
# * * * * *


# for i in range(1,6):
#     for j in range(1,i+1):
#         print("*",end="")
#     print("")


# # 6) WAP to calculate sum and average of a given array: arr=(‘i’,[1,2,3,4,5]).

# import array as arr

# myarray = arr.array('i',[1,2,3,4,5])
# add=0
# for i in range(0,len(myarray)):
#     add+=myarray[i]
# print("Average", add/len(myarray))




# # 7) Create a function to check whether number is prime or not.

# n = int(input("Enter the number: "))

# for i in range(2,n):
#     if n%i==0:
#         print("Not a prime number")
#         break
#     if i == n-1:
#         print("number is prime")
#         break
#     else:
#         i+=1


# 9) WAP to check whether the string is palindrome or not.

# # Function to check if a string is a palindrome
# def is_palindrome(s):
#     # Convert the string to lowercase for case-insensitive comparison
#     s = s.lower()
    
#     # Check if the string is equal to its reverse
#     if s == s[::-1]:
#         return True
#     else:
#         return False

# # Input string
# string = input("Enter a string: ")

# # Check if the string is palindrome and display the result
# if is_palindrome(string):
#     print(f"'{string}' is a palindrome.")
# else:
#     print(f"'{string}' is not a palindrome.")



# 10) WAP to create a user defined function to calculate sum of variable number of
# arguments using the concept of variable length argument in function.

# # Define a function to calculate sum of variable number of arguments
# def calculate_sum(*args):
#     return sum(args)

# # Test the function with different numbers of arguments
# print("Sum of 1, 2, 3:", calculate_sum(1, 2, 3))           # Output: 6
# print("Sum of 5, 10, 15, 20:", calculate_sum(5, 10, 15, 20)) # Output: 50
# print("Sum of 7, 14:", calculate_sum(7, 14))                # Output: 21



# # 12) WAP to calculate square of a number from 1 to 10 using list comprehension.

# square = [x**2 for x in range(1,11)]
# print(square)


# # 15) Use dictionary comprehension to create a dictionary to store only key value
# # pairs having even age.

# original_dict = {'jack': 38, 'michael': 48, 'guido': 57, 'john': 33}
# # Original dictionary
# original_dict = {'jack': 38, 'michael': 48, 'guido': 57, 'john': 33}

# # Using dictionary comprehension to filter only even ages
# even_age_dict = {key: value for key, value in original_dict.items() if value % 2 == 0}

# # Display the new dictionary
# print(even_age_dict)


# 18) Write a Python class named Circle. Declare an instance variable, radius and
# two methods that will compute the area and the perimeter of a circle.

# import math

# # # Define the Circle class
# class Circle:
#     # Constructor to initialize radius
#     def __init__(self, radius):
#         self.radius = radius
    
#     # Method to calculate area of the circle
#     def area(self):
#         return math.pi * self.radius ** 2
    
#     # Method to calculate perimeter (circumference) of the circle
#     def perimeter(self):
#         return 2 * math.pi * self.radius

# # Create an instance of Circle with a specific radius
# circle = Circle(5)

# # Call the methods and display the results
# print(f"Area of the circle: {circle.area()}")
# print(f"Perimeter of the circle: {circle.perimeter():.2f}")



# # 22) WAP to demonstrate how to use lambda in map() function.
# # Example list of numbers
# numbers = [1, 2, 3, 4, 5]

# # Using lambda to square each number in the list using map()
# squared_numbers = map(lambda x: x**2, numbers)

# # Convert map object to a list and print the result
# print(list(squared_numbers))



# 23) WAP to demonstrate how to use lambda in filter() function.

# # Example list of numbers
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# # Using lambda to filter out only even numbers from the list using filter()
# even_numbers = filter(lambda x: x % 2 == 0, numbers)

# # Convert filter object to a list and print the result
# print(list(even_numbers))



# 24) WAP to demonstrate how to define class method and static method in a class.

# class MyClass:
#     # Constructor to initialize the instance variable
#     def __init__(self, name):
#         self.name = name

#     # Class method (bound to the class)
#     @classmethod
#     def class_method(cls):
#         print("This is a class method. Class:", cls)

#     # Static method (not bound to the class or instance)
#     @staticmethod
#     def static_method():
#         print("This is a static method. No self or cls parameter.")

#     # Instance method
#     def instance_method(self):
#         print(f"This is an instance method. Hello {self.name}!")


# # Create an instance of MyClass
# obj = MyClass("Alice")

# # Calling the instance method
# obj.instance_method()

# # Calling the class method using the class object
# obj.class_method()  # You can also call this directly from the class like MyClass.class_method()

# # Calling the static method using the class object
# obj.static_method()  # You can also call this directly from the class like MyClass.static_method()

# # Calling the class method directly from the class without an object
# MyClass.class_method()

# # Calling the static method directly from the class without an object
# MyClass.static_method()





# 25) Create a GUI application to add two numbers using Label, Entry and Button
# widgets.

import tkinter as tk

# Function to add two numbers
def add_numbers():
    try:
        # Getting the values from Entry widgets
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        
        # Calculating the sum
        result = num1 + num2
        
        # Displaying the result
        label_result.config(text="Result: " + str(result))
    except ValueError:
        # Error message if input is invalid
        label_result.config(text="Please enter valid numbers")

# Creating the main window
root = tk.Tk()
root.title("Add Two Numbers")

# Creating Labels
label_num1 = tk.Label(root, text="Enter first number:")
label_num1.grid(row=0, column=0)

label_num2 = tk.Label(root, text="Enter second number:")
label_num2.grid(row=1, column=0)

label_result = tk.Label(root, text="Result:")
label_result.grid(row=3, column=0, columnspan=2)

# Creating Entry widgets to accept user input
entry_num1 = tk.Entry(root)
entry_num1.grid(row=0, column=1)

entry_num2 = tk.Entry(root)
entry_num2.grid(row=1, column=1)

# Creating a Button to perform the addition
button_add = tk.Button(root, text="Add", command=add_numbers)
button_add.grid(row=2, column=0, columnspan=2)

# Running the GUI application
root.mainloop()
