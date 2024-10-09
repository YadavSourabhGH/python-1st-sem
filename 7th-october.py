# build in function in pythin 

# py documentation : https://docs.python.org/3/library/stdtypes.html#string-methods

# s1 = 'Python Programming is cool'
# string are immutable / do not change when functions are applied
# print(s1)
# print(s1.lower())
# print(s1.upper())
# print(s1.title())
# print(s1.capitalize())

# output:
# Python Programming is cool
# python programming is cool
# PYTHON PROGRAMMING IS COOL
# Python Programming Is Cool
# Python programming is cool



# print(s1.isupper())
# print(s1.islower())
# print(s1.istitle())
# print(s1.isalpha())
# print(s1.isdigit())

# output:
# False
# False
# False
# False
# False



# print(s1.center(30,"#"))
# print(s1.count('o'))
# print(s1.count('o',5))
# print(s1.count('o',5,10))
# print(s1.startswith("Py"))
# print(s1.startswith("py"))
# print(s1.endswith("ool"))

# output:
# ##Python Programming is cool##
# 4
# 3
# 1
# True
# False
# True


# print(s1.find("c")) #output: 22
# print(s1.find("c",5,10)) #output: -1
# if data is not found then output will be -1 which means not found

# print(s1.index("c")) #output: 22
# print(s1.index("c",5,10)) #output: error

# print(s1.replace("c","p"))

# v1='ofsao'
# print(v1.isidentifier())
# as1="0e10"
# print(as1.isascii())
# print("0e10")


# l1=["ITM",",","BTECH",",","CSE"]
# print("".join(l1))
# output : ITM,BTECH,CSE

# s2="ITM,BTECH,CSE"
# print(s2.split(","))
# output : ['ITM', 'BTECH', 'CSE']

# print(s2.split(",",maxsplit=1))
# output : ['ITM', 'BTECH,CSE']

# print(chr(97)) #output : a

# msg = '''hello
# sourabh
# how
# are you?'''


# print(msg.splitlines()) #output : ['hello', 'sourabh', 'how', 'are you?']

# print("           techy".strip()) #output : techy

# s3 = '!!!!  Hello !!!'
# print(s3.strip("!").strip())


# Array in Python

# list is hetrogenious (can store any data type in one)
# array are homogenious (can store one 1 data type in one array)

import array as arr #import name as alias(optional)

# a1=arr.array("d",[1.1,3.5,4.5])
# # print(arr.array("d",[]),)
# print("first element :\t",a1[0])
# print("second element :",a1[1])
# print("last element :\t",a1[-1])

l2=[45,43,23,90,5,34,54,5,4,32,5,4,2]
list_to_array = arr.array("i",l2)
# print(list_to_array)

# print(list_to_array[:-5])

# list_to_array.insert(0,100)

# print(list_to_array)



# print(list_to_array.remove(5))

# pop remove from index no and remove remove the element  

# search an element in array 
x = int(input("To find : "))
if x in list_to_array:
    print("Yes")
else:
    print("No")