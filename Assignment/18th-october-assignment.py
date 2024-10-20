# # 1. Write a Python class that has two methods: get_String and print_String , get_String accept a string from the user and print_String prints the string in upper case.

# class string_uppercase:
#     string=""

#     def get_String(self):
#         self.string=input("Enter the String : ")
#     def print_String(self):
#         print(self.string.upper())

# try1=string_uppercase()
# try1.get_String()
# try1.print_String()




# # 2. Write a Python program to create a calculator class. Include methods for basic arithmetic operations.

# class Calc:
#     def __init__(self):
#         self.num1 = 0
#         self.num2 = 0

#     def take_nums(self):
#         self.num1 = float(input("Enter 1st Number: "))
#         self.num2 = float(input("Enter 2nd Number: "))

#     def add(self):
#         return self.num1 + self.num2

#     def sub(self):
#         return self.num1 - self.num2

#     def div(self):
#         if self.num2 != 0:
#             return self.num1 / self.num2
#         else:
#             return "Division by zero is not allowed."

#     def multi(self):
#         return self.num1 * self.num2

#     def output(self, operator):
#         if operator == "+":
#             print("Result:", self.add())
#         elif operator == "-":
#             print("Result:", self.sub())
#         elif operator == "/":
#             print("Result:", self.div())
#         elif operator == "*":
#             print("Result:", self.multi())
#         else:
#             print("Invalid operator.")

# try2 = Calc()
# try2.take_nums()
# try2.output(input("Enter operation (+, -, /, *): "))




# # 3. Write a Python class named Circle constructed from a radius and two methods that will compute the area and the perimeter of a circle.

# import math

# class Circle:
#     def __init__(self, radius):
#         self.radius = radius

#     def area(self):
#         return math.pi * self.radius ** 2

#     def perimeter(self):
#         return 2 * math.pi * self.radius

# radius = float(input("Enter the radius of the circle: "))
# circle = Circle(radius)

# print("Area of the circle: ", circle.area())
# print("Perimeter of the circle: ", circle.perimeter())




# # 4. Write a Python class to implement pow(x, n).

# class Power:
#     def __init__(self, base, exponent):
#         self.base = base
#         self.exponent = exponent

#     def compute_power(self):
#         return self.base ** self.exponent


# base = float(input("Enter the base (x) : "))
# exponent = int(input("Enter the exponent (n) : "))
# power_calculator = Power(base, exponent)

# print(f"{base} raised to the power of {exponent} is:", power_calculator.compute_power())



# # 5. Write a Python program to create a class representing a shopping cart. Include methods for adding and removing items, and calculating the total price.

# class ShoppingCart:
#     def __init__(self):
#         self.cart = {} 

#     def add_item(self, item_name, price):
#         if item_name in self.cart:
#             print(f"{item_name} is already in the cart.")
#         else:
#             self.cart[item_name] = price
#             print(f"{item_name} added to the cart.")

#     def remove_item(self, item_name):
#         if item_name in self.cart:
#             del self.cart[item_name]
#             print(f"{item_name} removed from the cart.")
#         else:
#             print(f"{item_name} is not in the cart.")

#     def total_price(self):
#         total = sum(self.cart.values())
#         return total

#     def show_cart(self):
#         if not self.cart:
#             print("Your cart is empty.")
#         else:
#             print("Shopping Cart Items:")
#             for item, price in self.cart.items():
#                 print(f"{item}: ${price:.2f}")

# cart = ShoppingCart()

# while True:
#     print("\n1. Add item\n2. Remove item\n3. Show cart\n4. Total price\n5. Exit")
#     choice = int(input("Enter your choice: "))

#     if choice == 1:
#         item_name = input("Enter item name: ")
#         price = float(input(f"Enter price for {item_name}: "))
#         cart.add_item(item_name, price)
#     elif choice == 2:
#         item_name = input("Enter item name to remove: ")
#         cart.remove_item(item_name)
#     elif choice == 3:
#         cart.show_cart()
#     elif choice == 4:
#         print(f"Total price: ${cart.total_price():.2f}")
#     elif choice == 5:
#         break
#     else:
#         print("Invalid choice. Please try again.")




# # 6. Write a Python class Employee with attributes like emp_id, emp_name,
# # emp_salary, and emp_department and methods like
# # calculate_emp_salary, emp_assign_department, and
# # print_employee_details.

# class Employee:
#     def __init__(self, emp_name, emp_id, emp_salary, emp_department):
#         self.emp_name = emp_name
#         self.emp_id = emp_id
#         self.emp_salary = emp_salary
#         self.emp_department = emp_department

#     def assign_department(self, new_department):
#         self.emp_department = new_department
#         print(f"{self.emp_name} has been assigned to the {new_department} department.")

#     def calculate_emp_salary(self, hours_worked):
#         if hours_worked > 50:
#             overtime_hours = hours_worked - 50
#             overtime_amount = overtime_hours * (self.emp_salary / 50)
#             total_salary = self.emp_salary + overtime_amount
#         else:
#             total_salary = self.emp_salary

#         return total_salary

#     def print_employee_details(self):
#         print(f"Employee Name: {self.emp_name}")
#         print(f"Employee ID: {self.emp_id}")
#         print(f"Employee Salary: ${self.emp_salary:.2f}")
#         print(f"Employee Department: {self.emp_department}")



# emp1 = Employee("ADAMS", "E7876", 50000, "ACCOUNTING")
# emp2 = Employee("JONES", "E7499", 45000, "RESEARCH")
# emp3 = Employee("MARTIN", "E7900", 50000, "SALES")
# emp4 = Employee("SMITH", "E7698", 55000, "OPERATIONS")


# emp1.print_employee_details()
# print()


# hours_worked = 55 
# print(f"Total salary for {emp1.emp_name} (with {hours_worked} hours worked): ${emp1.calculate_emp_salary(hours_worked):.2f}")
# print()

# emp1.assign_department("FINANCE")
# emp1.print_employee_details()




# # 7. Write a  Python class BankAccount with attributes like account_number, balance,
# # date_of_opening and customer_name, and methods like deposit, withdraw, and
# # check_balance.

# class BankAccount:
#     def __init__(self, account_number, customer_name, date_of_opening, balance=0):
#         self.account_number = account_number
#         self.customer_name = customer_name
#         self.date_of_opening = date_of_opening
#         self.balance = balance

#     def deposit(self, amount):
#         if amount > 0:
#             self.balance += amount
#             print(f"${amount} deposited successfully. New balance: ${self.balance:.2f}")
#         else:
#             print("Deposit amount must be positive.")

#     def withdraw(self, amount):
#         if amount > 0:
#             if self.balance >= amount:
#                 self.balance -= amount
#                 print(f"${amount} withdrawn successfully. New balance: ${self.balance:.2f}")
#             else:
#                 print("Insufficient balance.")
#         else:
#             print("Withdrawal amount must be positive.")

#     def check_balance(self):
#         print(f"Current balance: ${self.balance:.2f}")

#     def print_account_details(self):
#         print(f"Account Number: {self.account_number}")
#         print(f"Customer Name: {self.customer_name}")
#         print(f"Date of Opening: {self.date_of_opening}")
#         print(f"Current Balance: ${self.balance:.2f}")

# account = BankAccount("1234567890", "John Doe", "2024-01-15", 500)

# account.print_account_details()
# print()

# account.deposit(200)
# print()

# account.withdraw(100)
# print()

# account.check_balance()




# # 8. Create a class hierarchy for different types of geometric shapes, including circles,
# # rectangles, and triangles,

# import math

# class Shape:
#     def __init__(self, colour):
#         self.colour = colour

#     def calculate_area(self):
#         pass

#     def print_details(self):
#         print(f"Shape Colour: {self.colour}")
#         print(f"Shape Area: {self.calculate_area()}")

# class Circle(Shape):
#     def __init__(self, colour, radius):
#         super().__init__(colour)
#         self.radius = radius

#     def calculate_area(self):
#         return math.pi * self.radius ** 2

#     def print_details(self):
#         super().print_details()
#         print(f"Circle Radius: {self.radius}")

# class Rectangle(Shape):
#     def __init__(self, colour, length, width):
#         super().__init__(colour)
#         self.length = length
#         self.width = width

#     def calculate_area(self):
#         return self.length * self.width

#     def print_details(self):
#         super().print_details()
#         print(f"Rectangle Length: {self.length}")
#         print(f"Rectangle Width: {self.width}")

# class Square(Rectangle):
#     def __init__(self, colour, side_length):
#         super().__init__(colour, side_length, side_length)

#     def print_details(self):
#         super().print_details()
#         print(f"Square Side Length: {self.length}")

# class Parallelogram(Rectangle):
#     def __init__(self, colour, base, height):
#         super().__init__(colour, base, height)
#         self.base = base
#         self.height = height

#     def calculate_area(self):
#         return self.base * self.height

#     def print_details(self):
#         super().print_details()
#         print(f"Parallelogram Base: {self.base}")
#         print(f"Parallelogram Height: {self.height}")

# class Triangle(Shape):
#     def __init__(self, colour, base, height):
#         super().__init__(colour)
#         self.base = base
#         self.height = height

#     def calculate_area(self):
#         return 0.5 * self.base * self.height

#     def print_details(self):
#         super().print_details()
#         print(f"Triangle Base: {self.base}")
#         print(f"Triangle Height: {self.height}")

# print("Testing Circle:")
# circle = Circle("Red", 5)
# circle.print_details()

# print("\nTesting Rectangle:")
# rectangle = Rectangle("Blue", 4, 6)
# rectangle.print_details()

# print("\nTesting Square:")
# square = Square("Green", 4)
# square.print_details()

# print("\nTesting Parallelogram:")
# parallelogram = Parallelogram("Yellow", 5, 3)
# parallelogram.print_details()

# print("\nTesting Triangle:")
# triangle = Triangle("Purple", 6, 4)
# triangle.print_details()




# # 9. Create a Bus child class that inherits from the Vehicle class. The default fare charge of
# # any vehicle is seating capacity * 100. If Vehicle is Bus instance, we need to add an
# # extra 10% on full fare as a maintenance charge. So total fare for bus instance will
# # become the final amount = total fare + 10% of the total fare.
# # Note: The bus seating capacity is 50. so the final fare amount should be 5550.
# # You need to override the fare() method of a Vehicle class in Bus class.

# class Vehicle:
#     def __init__(self, seating_capacity):
#         self.seating_capacity = seating_capacity

#     def fare(self):
#         return self.seating_capacity * 100


# class Bus(Vehicle):
#     def __init__(self, seating_capacity=50):
#         super().__init__(seating_capacity)

#     def fare(self):
#         total_fare = super().fare()
#         maintenance_charge = total_fare * 0.10 
#         final_fare = total_fare + maintenance_charge
#         return final_fare

# bus = Bus()
# print(f"Bus fare: {bus.fare()}")
