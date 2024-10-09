# # Q1. print multiplication table of given number

# num = int(input("Enter the number : "))
# for i in range(1,11):
#     print(num,"x",i,"=",num*i)
# print("\nEnd")





# # Q2.  count the total number of digit in a number

# num = input("Enter a number : ")

# for i in range(1,len(num)+1):
#     pass
# print("total digits",i)





# # Q3.  print list in reverse order using a loop 

# l1 = [1,2,3,4,5,6,7,8,9,0]

# for i in range(len(l1),0,-1):
#     print(l1[i-1],end=" ")
# print("End")





# # Q4. print all prime number within a range 

# for i in range(1,25):
#     for j in range(2,i):
#         if(i%j==0):
#             break
#         if(i%j != 0):
#            print(i,end=" ")
#            break
# print("\nEnd")





# # Q5. display fibonacci series up to 10 

# cf=0
# cs=1
# csum=0
# fbvalues=[0]
# for i in range(1,10):
#     csum= cf+cs
#     fbvalues.append(csum)
#     cf = cs
#     cs = csum
# for j in range(0,len(fbvalues)):
#     print(fbvalues[j],end=", ")
# print("\nEnd")





# # Q6. reverse a interger number without using buildin function 

# number = int(input("Enter a number : "))
# reversed_number = 0
# while number>0:
#     last_digit = number%10
#     reversed_number=reversed_number*10+last_digit
#     number=number//10
# print(reversed_number)





# # Q7. Use for loop to iterate from 0 to 100 and print the sum of all evens and the sum of all odds.

# even_add = 0
# odd_add = 0
# for i in range(1,101):
#     if(i%2 == 0):
#         even_add=even_add+i
#     else:
#         odd_add=odd_add+i
# print("The sum of all even number from 1 to 100 is \"",even_add,"\" \nand the sum of all odd number from 1 to 100 is \"",odd_add,"\"")




# # Q8. Write a Python program that accepts a string and calculates the number of digits and letters. 

# import string 
# user_input = input("Enter the string : ")
# char = 0
# num = 0
# for i in range(0,len(user_input)):
#     if user_input[i] in string.digits:
#         num+=1
#     elif user_input[i].lower() in string.ascii_lowercase:
#         char+=1
# print(f'Number of Letters : {char}\nNumber of Digits : {num}')





# # Q9 a)

# for i in range(5,0,-1):
#     for j in range(i,0,-1):
#         print(j,end=" ")
#     print()
# # print("End")

# # Q9 b)

# for i in range(1,6):
#     for j in range(1,i+1):
#         print("*",end="")
#     print()
# for i in range(1,5):
#     for j in range(4,i-1,-1):
#         print("*",end="")
#     print()