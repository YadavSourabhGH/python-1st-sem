# # 1. Write a Python program to remove duplicates from a list.

# n = input("Enter elements for the list in this format(2 4 5 . .) : ").strip().split()
# shorted=[]
# for i in range(len(n)):
#     if n[i] not in n[:i]:
#         shorted.append(n[i])
#     else:
#         pass
# print(shorted)




# # 2. Write a Python function that takes two lists and returns True if they have at least one common member.

# n2 = input("Enter elements for the list in this format(2 4 5 . .) For 1st list : ").strip().split()
# n3 = input("Enter elements for the list in this format(2 4 5 . .) For 2nd list : ").strip().split()
# def main():
#     for i in range(len(n2)):
#         if n2[i] in n3:
#             return True
#     for i in range(len(n3)):
#          if n3[i] in n2:
#             return True
# print(True if main() else False)




# # 3. Write a Python program to print the numbers of a specified list after removing even numbers from it.

# n4 = input("Enter elements for the list in this format(2 4 5 . .) : ").strip().split()
# result=[]
# for i in range(len(n4)):
#     if int(n4[i]) % 2 != 0:
#         result.append(n4[i])
# print(result)




# # 4. Write a Python program to find the second smallest number in a list.

# n5 = input("Enter elements for the list in this format(2 4 5 . .) : ").strip().split()
# smallest = float('inf') #inf = infinite
# ssmall = float('inf') 

# for i in range(len(n5)):
#     n5[i] = int(n5[i])

# for n in n5:
#     if n < smallest:
#         ssmall = smallest 
#         smallest = n
#     elif n < ssmall and n != smallest:
#         ssmall = n

# if ssmall == float('inf'):
#     print("There is no second smallest number in the list.")
# else:
#     print("The second smallest number is:", ssmall)




# # 5. Write a Python program to split a list every Nth element.

# def split_list(lst, n):
#     result = []
#     for i in range(0, len(lst), n):
#         result.append(lst[i:i+n])
#     return result
# lst = input("Enter elements for the list in this format (1 2 3 4 ...): ").strip().split()

# for i in range(len(lst)):
#     lst[i] = int(lst[i])

# n6 = int(input("Enter the value of N: "))
# split_lst = split_list(lst, n6)
# print("List split every", n6, "elements:", split_lst) 




# # 6. Write a Python a function to find the union and intersection of two lists.

# n7 = input("Enter elements for the list in this format(2 4 5 . .) For 1st list : ").strip().split()
# n8 = input("Enter elements for the list in this format(2 4 5 . .) For 2st list : ").strip().split()

# s1=set(n7)
# s2=set(n8)
# print("Union :",s1.union(s2))
# print("Intersection :",s1.intersection(s2))




# # 7. Write a Python function to check if a list is a palindrome or not. Return true otherwise false.

# n9 = input("Enter elements for the list in this format (1 2 3 ...): ").strip().split()
# n9 = [int(num) for num in n9]

# if n9 == n9[::-1]:
#     print("The list is a palindrome.")
# else:
#     print("The list is not a palindrome.")
