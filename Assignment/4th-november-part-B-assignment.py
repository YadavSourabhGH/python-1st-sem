# # 1. Write a program to exhibit these concepts:
# #            i. try
# #            ii. except
# #            iii. finally

# def takeinput():
#     try:
#         num = int(input("Enter ONLY Number "))
#         print(num, "is num")
#     except ValueError:
#         print("Not a number")
#     finally:
#         print("End")
# takeinput()



# 2. Write a Python program to handle a ZeroDivisionError exception when dividing a number by zero.

# def example(val1,val2):
#     try:
#         res=val1/val2
#         return res
#     except ZeroDivisionError:
#         return "Error: cannot divide by zero"
#     finally:
#         # print("Responded")
#         pass
        
# print(example(1,1)) 
# print(example(3,0))


# print( 36/4 *(3+2)* 4+2) 
# 182.0

# 3. Write a Python program that prompts the user to input an integer and raises a ValueError exception if the input is not a valid integer.

# try:
#     if(int(input("Enter number:")).is_integer()):
#         print("Number detected")
# except ValueError:
#     print("Value error")
# finally:
#     print("END")




# # 4. WAP that exhibits multiple except blocks along with default block
# another_list=[]
# def loop(list,length):
#     try:
#         for i in range(length+1):
#             another_list[i]=list[i]
#     except IndexError:
#         print("Given Length is not correct")
#     except TypeError:
#         print("Length is not int")
#     except Exception as e:
#         print(e)
#     finally:
#         print("End")

# loop([1,2,3,4,5],"9") #Length is not int
# loop([1,2,3,4,5],6) #Length is not int




# # 5. WAP that exhibits except blocks that can catch multiple exceptions.

# another_list=[]
# def loop(list,length):
#     try:
#         for i in range(length+1):
#             another_list[i]=list[i]
#     except IndexError:
#         print("Given Length is not correct")
#     except TypeError:
#         print("Length is not int")
#     finally:
#         print("End")

# loop([1,2,3,4,5],"9") #Length is not int
# loop([1,2,3,4,5],6) #Length is not int