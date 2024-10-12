

# global_var = "Global Var"
# def fun(n):
#     local_var = "Local Var" #can be accessed inside the function only
#     global global_var2 # with this we can declare a global variable inside any function block
#     global_var2 = 20 # can be accessed abywhere in the code

# print(global_var)
# # print(local_var) #error
# print(global_var2)




# a = 20
# def scopeDemo():
#     a = 10
#     print("a =",globals()['a'])
#     print("a =",a)

# scopeDemo()




# recurssion is the process where function call itself from its own body and that function is called as recurrsive process


# def factorial(n):
#     if n == 1:
#         return 1
#     else:
#         return n*factorial(n-1)
    

# print(factorial(10))




# Python Module 

# import hellomodule as hello
# name= input("Name : ")
# hello.sayhello(name) 

# from hellomodule import goodnight as gb
# gb()



import math
import random
import time

# print(dir(math))
# print(math.pi)
# print(math.factorial(15))
# print(math.isqrt(25))  # Integer square root
# print(math.prod([1, 2, 3, 4]))  # Product of elements
# print(math.perm(5, 2))  # Permutation
# print(math.comb(5, 2))  # Combination
# print(math.remainder(10, 3))  # Remainder of division
# print(math.fmod(10, 3))  # Modulus of division
# print(math.exp(3))  # e^x
# print(math.expm1(3))  # e^x - 1
# print(math.log2(16))  # Log base 2
# print(math.log10(1000))  # Log base 10
# print(math.degrees(math.pi))  # Convert pi radians to degrees
# print(math.radians(180))  # Convert degrees to radians
# print(math.copysign(5, -3))  # Copy sign of second argument to the first
# print(math.fsum([0.1, 0.2, 0.3]))  # Accurate floating point sum
# print(math.dist([1, 2], [3, 4]))  # Distance between two points
# print(math.isfinite(1e309))  # Check if finite
# print(math.isinf(float('inf')))  # Check if infinite
# print(math.isnan(float('nan')))  # Check if NaN
# print(math.trunc(5.9))  # Truncate the decimal part
# print(math.modf(5.9))  # Split integer and fractional parts
# print(math.log1p(2))  # log(1+x)
# print(math.asin(0.5))  # Inverse sine
# print(math.acos(0.5))  # Inverse cosine
# print(math.atan(1))  # Inverse tangent
# print(math.atan2(1, 1))  # Four-quadrant inverse tangent
# print(math.sinh(1))  # Hyperbolic sine
# print(math.cosh(1))  # Hyperbolic cosine
# print(math.tanh(1))  # Hyperbolic tangent
# print(math.asinh(1))  # Inverse hyperbolic sine
# print(math.acosh(2))  # Inverse hyperbolic cosine
# print(math.atanh(0.5))  # Inverse hyperbolic tangent

# print(math.sqrt(16))  # Square root
# print(math.factorial(5))  # Factorial
# print(math.gcd(48, 60))  # Greatest common divisor
# print(math.sin(math.radians(30)))  # Sine of 30 degrees
# print(math.cos(math.radians(60)))  # Cosine of 60 degrees
# print(math.tan(math.radians(45)))  # Tangent of 45 degrees
# print(math.pi)  # Value of pi
# print(math.log(10))  # Natural logarithm (base e)
# print(math.pow(2, 3))  # 2 raised to the power of 3
# print(math.fabs(-7))  # Absolute value
# print(math.floor(7.9))  # Floor of a number
# print(math.ceil(7.9))  # Ceiling of a number
# print(math.radians(180))  # Degrees to radians
# print(math.degrees(math.pi))  # Radians to degrees
# print(math.hypot(3, 4))  # Hypotenuse of a right-angled triangle



# print(random.random())
# print(random.randint(5,10))
# print(random.random())
# a=[1,2,3,4,5,6,7,8,9,0]
# random.shuffle(a)
# print(a)



# develop a number gusser game with 3 change with score system
global score
score=0
times=0
print("Hello! Welcome to guess the number game!")
print("-"*50)
print("Generating Game...")
time.sleep(1.5)
print("I have picked a Random number from 0 to 10")
print("Score :",score)
num = random.randint(0,10)


def game():
    global score
    score=0
    user_input=int(input("Enter Your Gussed Number : "))
    if(times == 3):
        print("You Loose!")
        c=input("want to play again? (Y) or (N)").strip().lower()
        if c == "y":
            game()
        else:
            pass
    else:
       if user_input==num:
           print("Yaa Hoo! You Gussed it Correct!")
           print("-"*50)
           score+=10
           print("Score :",score)
           d=input("do you want To continue (Y) or (N)? : ")
           if d == "y":
               game()
           else:
               pass

       else:
            print("No! You are wrong")
            game()


game()