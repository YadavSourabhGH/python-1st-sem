# # Q1 python program to check wheather the string is symmertical or Palindrome

# s1 = input("Enter a string : ").lower().replace(" ","")
# if(s1 == s1[::-1]):
#     print("Its an Palindrome String")
# else:
#     print("Not a Palindrome string")




# # Q2. Find length of a string in python without using len function

# s2 = input("Enter a String : ").lower()
# count = 0
# for i in s2:
#     count += 1
# print(count)




# # Q3. Python Program to remove all duplicates from a given string

# s3 = input("Enter a String : ").lower()
# l1=[]
# for i in range(0,len(s3)):
#     if s3[i] == " ":
#         l1.append(s3[i])
#     elif s3[i] not in l1:
#         l1.append(s3[i])
# print("".join(l1))




# # Q4. Maximum frequency character in String

# s4 = input("Enter a string : ").lower()
# dict1 = {}
# for i in range(0,len(s4)):
#     if s4[i] in dict1:
#         dict1[f'{s4[i]}'] = dict1[s4[i]]+1
#     elif s4[i] == " ":
#         pass
#     else:
#         dict1[f'{s4[i]}'] = 1
# max_freq = max(dict1 ,key=dict1.get)
# print("Most Frequent Letter is ",max_freq,"with no of letter :",dict1[max_freq])




# # Q5. Write a Python program to count the number of characters in a string.

# s5 = input("Enter a string : ").lower()
# dict2 = {}
# for i in range(0,len(s5)):
#     if s5[i] in dict2:
#         dict2[f'{s5[i]}'] = dict2[s5[i]]+1
#     elif s5[i] == " ":
#         pass
#     else:
#         dict2[f'{s5[i]}'] = 1
# print(dict2)




# # Q6. Count all letters, digits, and special symbols from a given string

# s6 = input("Enter a String : ").lower()
# l,d,s=0,0,0
# for i in range(0,len(s6)):
#     if s6[i].isalpha():
#         l+=1
#     elif s6[i].isnumeric():
#         d+=1
#     elif s6[i] == " ":
#         pass
#     else:
#         s+=1
# print(f'Letters : {l}, Digits : {d}, Special Characters : {s}')




# # Q7. Write a program which read incoming email, all emails not sent from the "@itm.edu" domain should be moved to the spam box.

# n1 = int(input("Enter Number Of Emails : "))
# all_emails = []
# spam_emails = []
# itm_emails = []
# for i in range(n1):
#     all_emails.append(input(f'Enter Email [{i+1}] : ').strip())
# for sort_email in all_emails:
#     if "@itm.edu" in sort_email:
#         itm_emails.append(sort_email)
#     else:
#         spam_emails.append(sort_email)
# print("\nITM.EDU Emails : ")
# for email in itm_emails:
#     print(email)
# print("\nSPAM EMAILS : ")
# for email in spam_emails:
#     print(email)




# # Q8. You are tasked to create a simple password validator. The validation rules are as follows:
# # Password length of at least 8 characters.
# # At least one uppercase character.
# # At least one lowercase character.
# # At least one "special" character from the following set of characters: "!#$%&*+-.?~"

# s7 = input("Enter Password : ").strip()
# l,u,lo,s,=0,0,0,0
# l = len(s7)
# s_chars = "! # $ % * + - . ? ~".split()
# if l<8:
#      print("Min 8 Characters Required!")
# else:
#     for i in range(0,l):
#         if s7[i].isupper(): u+=1
#         if s7[i].islower(): lo+=1
#         if s7[i] in s_chars: s+=1
#     if(l<1):print("Min 1 Lowercase Character Requiured!")
#     if(u<1):print("Min 1 Uppercase Character Requiured!")
#     if(s<1):print("Min 1 Special Character Requiured!")
#     if(s>=1 and u>=1 and l>=1):print("Valid Password!")
    
    