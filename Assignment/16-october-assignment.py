# # 1. Write a Python program to check if two given sets have no elements in common.

# s1 = set(input("Enter Values for 1st set in format (1 2 . .) : ").strip().split())
# s2 = set(input("Enter Values for 2nd set in format (1 2 . .) : ").strip().split())
# print("No common elements found!" if s1.isdisjoint(s2) else "Yes Common elements found!")





# 2. Write a Python program toGet Only unique items from two sets

# s1 = set(input("Enter Values for 1st set in format (1 2 . .) : ").strip().split())
# s2 = set(input("Enter Values for 2nd set in format (1 2 . .) : ").strip().split())
# print(s1.symmetric_difference(s2) if s1.symmetric_difference(s2) else "No Unique elements found!")





# # 3. Write a Python program to Convert Set to one String

# s1 = set(input("Enter set values in format (1 2 . .) : ").split())
# String=""
# for i in s1:
#     print(i,end=" ")




# # 4. program to count number of vowels using sets in given string

# vowel = set(['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'])
# s1 = set(input("Enter string for set : ").strip().split())
# count=0
# for i in s1:
#     if i in vowel:
#         count+=1
# print("No. of vowels :",count)
        



