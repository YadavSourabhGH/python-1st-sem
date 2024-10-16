# # dict

# # string , tupple is immutable
# # set, list. dict is mutable

# # Dictionary Operations

# D={} #creates an empty dictionary or {}
# D={'rollno': 142, 'name': 'Anurag', 'age':26} 
# # D=dict('rollno'=142, 'name'="Anurag", 'age'=26)
# print(D)


# thisdict = { 'brand': "Ford", 'model': "Mustang", 'year': 1964} 
# x = thisdict["model"]
# print(x)
# # Both the above statements make a dictionary having 3 key-value pairs.
# print(D['rollno']) #prints 142
# D['age']=28
# print(D) #changes value of 'age' key to 28
# # del(D['age']) # delete the element of following key
# print(D)

# # functions in dict : clear, copy, len(dict), str(dict), pop(), popitem(), keys(), values(), items(), get() 

# student2=D.copy()
# print(student2)
# print(str(D),type(str(D)))
# # print(D.popitem()) #by default remove last element but if we use pop we have to mention key
# print(D)
# print(D.keys())
# print(D.values())
# print(D.items())
# print(D.get('rollno'))
# # D.update()
# print(D)
# print(sorted(D))
# print(list(reversed(D)))