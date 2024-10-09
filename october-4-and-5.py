#loops

# while loop 
# for loop

# while(condition):
#     code to execute (when true)
# code to execute (when flase)




#decrement
# i = 10 #counter #step 1
# while(i>=1): #comdition #step 2
#         print(i,end=" ") #step 3
#         i=i-1 #decrement #step4, after step 4 go to step 2
# print("End Of Loop") #false statement


# i = 1 #counter #step 1
# while(i<=1): #comdition #step 2
#         print(i,end=" ") #step 3
#         i=i+1 #increment #step4, after step 4 go to step 2
# print("End Of Loop") #false statement

# # print("program end")
# nageswar rao


# for loop
#list, tupple, set - sequences

# for i in range(1,11):
#         print(i,end=" ")
# print("\nEND")
# #output 
# 1 2 3 4 5 6 7 8 9 10 
# END

# upto_number = int(input("Upto what number you want to print : "))
# for i in range(1 , upto_number+1 , 2):
# for i in range(11):
# for i in range(upto_number+1):


#         print(i,end=" ")
# print("\nEND")

# for i in range(10,0,-1):

#         print(i,end=" ")
# print("\nEND")


# list1 = [1,3,2,4,6,4,3,5,6,3,2,5,2,3,4,5,3,2,6,7,4,8,4,8,7]
# sum1 = 0
# for i in list1:
#    sum1=sum1+i
# print("Sum : ",sum1)

# factorialnum = int(input("Enter The Number : "))
# calc=1
# for i in range (factorialnum,0,-1):
#     print(i,"*",end=" ")
#     calc=calc*i
# print("\nFactotial Of ",factorialnum," is ",calc)

# october 5 

# l1 = [10,20,30,40,50,60]
# a = len(l1)
# i = 0
# while (i<a):
#     print(l1[i],end=" ") 
#     i=i+1
# print("\nEnd")

# a=100
# while (a>=100 and a<=200):
#     print(a,end=" ")
#     a=a+1
# print("end")

# s1 = "computer"

# for i in s1:
#     print(i,end=" ")
# print("End")


# user will enter a statement find out how many words are in the statement

# statement = input("Enter the statement : ")
# wordcount = 1
# if(statement):
#    for i in statement:
#         if(i == " "):
#            wordcount = wordcount+1
#    print(wordcount)
# else:
#     print("0")

#alternative

# l1=statement.split()
# # print(l1)
# print(len(l1))


# for i in range (1,11):
#     if(i == 5):
#         break
#     print(i,end=" ")


# for i in range (1,11):
#     if(i == 5):
#         continue
#     print(i,end=" ")
# print("end")

# to print all odd nummber between 1 to 100

# for i in range(1,101):
#     if(i%2 == 0):
#         continue
#     print(i,end=",")
# print("end")

# prime number

# n = int(input("Enter the number : "))
# flag=True 

# for i in range(2,n):
#     if(n%i == 0):
#         flag=False
#         print("not a prime number")
#         break
# if(flag==True):
#     print("Prime number")


# for i in range(1,101):
#     if(i%2 == 0):
#         pass # if we dont put anything in if block then it will give error to handle that error we use pass as do nothing
#         # print("pass")
#     else:
#         print(i,end=" ")
# print("\nEnd")


# for i in range(1,6):
#     for j in range(1,6):
#         print("*",end=" ")
#     print('')


# for i in range(1,6):
#     for j in range(1,i+1):
#         print("*",end=" ")
#     print('')
#  iiiii
# j*
# j**
# j***
# j****
# j*****


# for i in range(5,0,-1):
#     for j in range(1,i+1):
#         print("*",end=" ")
#     print('')

# for i in range(1,6):
#       for k in range(5,i,-1):
#             print(" "*k)
#             for j in range(1,i+1):
#                  print("*",end=" ")


# print('''Hello word
# 2nd line
# 3rd line
# 4th line''') # multiline string """" """" or ''' '''

# reverse indexing
# l1 = [1,2,3,4,5,6,7,8]
# print(l1[-1])

# forward indexing
# 0,1,,2,3,4...
# reverse indexing
# -1,-2,-3...


# slicing
# default values
# start= 0
# end= -1

str = "sourabh"
print(str[1:3])
print(str[-1:-5:-1])
print(str[1:-1])
print(str[1:-1:2])
print(str[::-1])
# print("hello \f world")
# print("hello \r world")
# print("hello \v world")
# print("hello \t world")
# print("hello \b world")





