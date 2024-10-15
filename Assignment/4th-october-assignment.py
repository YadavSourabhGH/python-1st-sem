# # take year and tell if it a leap year 
# year = int(input("Enter the Year : "))
# if(year % 4 == 0):
#     print("This is a leap year")
# elif(year % 4 != 0):
#     print("This is not a leap year")
# else:
#     print("Invalid Input")




#check if number enterd is 3 digit

# num = input("Enter the number : ")

# if(len(num) == 3):
#     print("its a 3 digit number")
# else:
#     print("not a 3 digit number")




# #program to check person is eligible for voting (voting age >= 18)
# age = int(input("Enter Your Age : "))
# if(age >= 18):
#     print("You are eligible for voting")
# else:
#     print("Not Eligible")




# #program to check if wether the last digit of number is 3

# num = input("Enter the Number : ")

# if(num[-1] == "3"):
#     print("yes Last digit is 3")
# else:
#     print("last digit is not 3")




# #program to check wether an alphabert is vowel or consonant

# alphabet = input("Enter a Alphabet : ").lower()
# vowel = ["a","e","i","o","u"]
# if(alphabet in vowel):
#     print("Its a vowel")
# else:
#     print("not a vowel")




# #program to convert month name to number of days

# month = input("Enter The Month (Jan, Feb Mar, Apr, May, June, July, Aug, Sept, Oct, Nov, Dec): ").lower()
# #31 days - jan mar may july aug oct dec
# month31days = ["jan","mar","may","july", "aug", "oct","dec"]

# if(month in month31days):
#     print("This Month have 31 days")
# elif(month == "feb"):
#     print("28 or 29 days")
# else:
#     print("Month have 30 days")




# # check if the triangle is equilatral, isosceles, scalene

# side1,side2,side3 = input("Enter Sides of triangle (eg: 5 9 2) : ").split()
# if(side1==side2==side3):
#     print("Its an Equilatral Triangle")
# elif(side1!=side2!=side3):
#     print("Its an Scalene Triangle")
# elif(side1 == side2 or side2 == side3 or side3 == side1):
#     print("Its An Isosceles Triangle")
# else:
#     print("Not Any Type")




# #program to calculate electricity bill ,1st 100 units free, 2nd 100 unit 5rs per unit, 3rd 100 units 10 rs per unit

# unit = int(input("Enter UNITS Used : "))

# if(unit<=100):
#     print("Electricity Bill : 0")
# elif(unit>100 and unit<=200):
#     paidunit = unit - 100
#     topay = paidunit*5
#     print("Electricity Bill : ",topay)
# elif(unit>200):
#     freeunit = unit-100 #free
#     paid_5rs_unit= freeunit - 100 #paid unit rs 5
#     topay_5rs = 100*5 
#     topay_final = paid_5rs_unit*10+topay_5rs
#     print("Electricity Bill : ",topay_final)




# #program to accept cost price and tell road tax to be paid
# # > 100,000 tax=15%
# # > 50,000 and <= 100,000 tax=10%
# # <= 50000 tax=5%

# cost = int(input("Enter the cost price of the bike : "))

# if(cost <= 50000):
#     tax = 5/100
#     tax_topay = cost*tax
#     print("Road Tax : ",tax_topay)
# elif(cost > 50000 and cost <= 100000):
#     tax=10/100
#     tax_topay = cost*tax
#     print("Road Tax : ",tax_topay)
# elif(cost > 100000):
#     tax=15/100
#     tax_topay = cost*tax
#     print("Road Tax : ",tax_topay)




# #program to accept the marked price from the user and calculate the net amount as (marked price - discount) to pay according to following
# # marked price        discount
# # >10000                20%
# # >7000 and <= 10000    15%
# # <=7000                10%

# price = int(input("Enter the marked price : "))

# if(price > 10000):
#     discount = 20/100 #20 %
#     to_pay = price - price*discount
#     print(f'Total Price \t: {price}\nDiscount \t: {price*discount}\nTo Pay \t: {to_pay}')
# elif(price > 7000 and price <= 10000):
#     discount = 15/100 #15 %
#     to_pay = price - price*discount
#     print(f'Total Price \t: {price}\nDiscount \t: {price*discount}\nTo Pay \t: {to_pay}')
# elif(price <= 7000):
#     discount = 10/100 #10 %
#     to_pay = price - price*discount
#     print(f'Total Price \t: {price}\nDiscount \t: {price*discount}\nTo Pay \t: {to_pay}')
# else:
#     print("Unexpected error")



