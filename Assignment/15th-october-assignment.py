# #1. Write a Python program to compute the element-wise sum of given tuples.

# n1=input("Enter values for tupple in this format 1st (1 2 3 . . .) : ").strip().split()
# n2=input("Enter values for tupple in this format 2nd (1 2 3 . . .) : ").strip().split()
# n3=input("Enter values for tupple in this format 3rd (1 2 3 . . .) : ").strip().split()
# t1 = tuple(map(int, n1))
# t2 = tuple(map(int, n2))
# t3 = tuple(map(int, n3))
# highest_tuple = max(len(t1), len(t2), len(t3))
# add=[]
# for i in range(0, highest_tuple):
#     add.append(t1[i] if i < len(t1) else 0)
#     add[i]+=t2[i] if i < len(t2) else 0
#     add[i]+=t3[i] if i < len(t3) else 0
# print(add)




# #2. Write a Python program to convert a given list of tuples to a list of lists.

# n = int(input("Enter No. of tupples you want to add : ").strip())
# lists=[]
# for i in range(0,n):
#     lists.append(input(f'Enter values for tupple ({i}) in this format (1 2 . .): ').strip().split())
# l = list(lists)
# print(l)




# # 3. Convert the said list of tuples to a list of lists: [[1, 2], [2, 3], [3, 4]]

# tuple = [(1, 2), (2, 3), (3, 4)]
# listoflist = []
# for t in tuple:
#     listoflist.append(list(t))
# print(listoflist)




# # 4. Write a Python program to remove an empty tuple(s) from a list of tuples.

# def remptytuples(tuple_list):
#     return [t for t in tuple_list if t]
# tuple = [(), (1, 2), (), (3, 4), (5,)]
# filter = remptytuples(tuple)

# print(filter)





# # 5. Write a Python program to convert a given string to a tuple

# def stringtotuple(s):
#     return tuple(s)
# inputstring = input("Enter String : ")
# resulttuple = stringtotuple(inputstring)

# print(resulttuple)




# 6. Write a Python program to calculate the product, multiplying all the numbers in a given tuple.


# def multiply(t):
#     product = 1
#     for num in t:
#         product *= num
#     return product

# tuple = (2, 3, 5)
# product = multiply(tuple)

# print("The product of the numbers in the tuple is:", product)






