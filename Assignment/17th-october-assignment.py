# # 1. Write a Python program to remove duplicates from the dictionary. 

# result_dict={}
# seenValues=set()
# def removeDuplicates(main_dict):
#     for key, value in main_dict.items():
#         if value not in seenValues:
#             result_dict[key]=value
#             seenValues.add(value)
#     return result_dict

# tempDict={'a':1,
#           'b':2,
#           'c':2,
#           'd':2,
#           'e':3}

# print(removeDuplicates(tempDict))




# # 2. Write a Python program to combine two dictionary by adding values for common keys.

# def combinedicts(dict1, dict2):
#     combined = dict1.copy()
    
#     for key, value in dict2.items():
#         if key in combined:
#             combined[key] += value
#         else:
#             combined[key] = value
    
#     return combined

# dict1 = {'a': 5, 'b': 10, 'c': 15}
# dict2 = {'b': 20, 'c': 25, 'd': 30}

# combined_dict = combinedicts(dict1, dict2)
# print("Combined dictionary:", combined_dict)




# # 3. Write a Python program to create a dictionary from a string. ( Track the count of the letters from the string.)

# def countletters(string):
#     lettercount = {}
    
#     for char in string:
#         if char.isalpha(): 
#             char = char.lower() 
#             if char in lettercount:
#                 lettercount[char] += 1
#             else:
#                 lettercount[char] = 1
                
#     return lettercount


# string = input("Enter String : ")
# print(countletters(string))




# # 4. Write a Python program to match key and values both, in two dictionaries.

# def match(dict1, dict2):
#     matcheditems = {}
    
#     for key, value in dict1.items():
#         if key in dict2 and dict2[key] == value:
#             matcheditems[key] = value
            
#     return matcheditems

# dict1 = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
# dict2 = {'a': 1, 'b': 5, 'c': 3, 'e': 6}
# matched = match(dict1, dict2)

# print("Matched key value pairs:", matched)


