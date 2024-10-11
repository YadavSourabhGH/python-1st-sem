import array as arr
import time
import random
import math

# 1.  Write a Python function to check whether a number falls within a given range.

# user_range_lower=int(input("Enter the range (lower) : "))
# user_range_higher=int(input("Enter the range (higher) : "))

# def check(n):
#     if n in range(user_range_lower , user_range_higher+1):
#         return True
#     else:
#         return False

# num = int(input("Enter the numbers : "))
# print(f'Yes, the number {num} is in range {user_range_lower , user_range_higher}' if check(num) else f'No, the number {num} is not in range {user_range_lower , user_range_higher}')




# 2. Write a Python function that takes a list of strings as input and returns a tuple containing the shortest and longest word from the list

# def finder(words):
#     shortest = min(words, key=len)
#     longest = max(words, key=len)
#     return (shortest, longest)

# words_list = input("Enter a string : ").strip().split()
# result = finder(words_list)
# print(f'Shortest : {result[0]}, longest : {result[1]}')




# 3.    Write a Python function that takes a list and an element as input. The function should add the element to the list only if it's not already present in the list.

# def add_if_not_present():
#     user_input = input("Enter elements of the list separated by spaces: ")
#     lst = user_input.split()

#     element = input("Enter the element to add: ")
#     if element not in lst:
#         lst.append(element)

#     print("Updated list:", lst)

# add_if_not_present()




# 4.    Write a program to implement these formulae of permutations and combinations. 
# Number of permutations of n objects taken r at a time: p(n, r) = n! / (n-r)!.
# Number of combinations of n objects taken r at a time is: c(n, r) = n! / (r!*(n-r)!) = p(n,r) / r!

# def factorial(n):
#     fact = 1
#     for i in range(1, n+1):
#         fact *= i
#     return fact

# def permutation(n, r):
#     return factorial(n) // factorial(n - r)
# def combination(n, r):
#     return permutation(n, r) // factorial(r)

# n = int(input("Enter the value of n: "))
# r = int(input("Enter the value of r: "))

# print(f"Permutations P({n}, {r}) = {permutation(n, r)}")
# print(f"Combinations C({n}, {r}) = {combination(n, r)}")




# 5.    A number is called perfect if the sum of proper divisors of that number is equal to the number. For example 28 is perfect number, since 1+2+4+7+14=28. Write a program to print all the perfect numbers in a given range

# def is_perfect(num):
#     divisor_sum = 0
#     for i in range(1, num):
#         if num % i == 0:
#             divisor_sum += i
#     return divisor_sum == num

# start = int(input("Enter the start of the range: "))
# end = int(input("Enter the end of the range: "))

# print(f"Perfect numbers between {start} and {end}:")
# for num in range(start, end + 1):
#     if is_perfect(num):
#         print(num)




# 6.    Write a recursive function that will return the nth term of the Fibonacci sequence.
# The sequence has a relationship of Fn = Fn-1 + Fn-2 with F0 = 0 and F1 = 1, where n=0,1,2,3,4,5,...

# def fibonacci(n):
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         return fibonacci(n-1) + fibonacci(n-2)

# n = int(input("Enter the term number to find in Fibonacci sequence: "))

# print(f"The {n}th term of Fibonacci sequence is: {fibonacci(n)}")

