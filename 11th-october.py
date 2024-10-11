# #list

# L1=[]
# type(L1)
# L2=list([1,2,3,4,5])
# print(L2)
# L3=["A","H","H","C"]
# print(L3)
# L4=[13,"sourabh","sourabhyadav9012@gmail.com",160000]
# print(L4)
# L4[2]="sourabh@mail.pro"
# print(L4)





# L5=[0,0,0,0,0]
# for i in range(0,5):
#     a = input(f'Enter the number {i+1} : ')
#     L5[i]=a
# print(L5)

# del L5[2:3] #delete index
# del L5[1]#delete index
# L5.pop(2)#delete index

# L5.remove(2)#delete element

# L5.pop()#remove last element if no arg is provided
# print(L5)


L6=[1,4,5,6,7,3]
# L6.append(40)
# print(L6)#[10, 20, 30, 40]
# L6.append([50,60])
# print(L6)#[10, 20, 30, 40, [50, 60]]

# print(L6.count(20))#1
# print(L6[4].count(50))#1
# L6.extend([70,80])
# L6.append(40)
# print(L6)
# print(L6.index(40)) # to find the data


# print(L6.index(40,4))

# L6.insert(5,35)
# print(L6) #[10, 20, 30, 40, [50, 60], 35, 70, 80, 40]

# L6.insert(6,[35,40])
# print(L6) #[10, 20, 30, 40, [50, 60], 35, [35, 40], 70, 80, 40]

# L6.reverse()
# print(L6) # [40, 80, 70, [35, 40], 35, [50, 60], 40, 30, 20, 10]
# print(list(reversed(L6)))
# # L6.clear()#remove all element from list
# L6.sort()
# print(L6)


# # below list contains square of all # odd numbers from range 1 to 10 
# odd_square = [x ** 2 for x in range(1, 11) if x%2 ==1]
# print(odd_square)


# odd_square = [] 
# for x in range (1, 11):
#     x%2 ==1 
#     odd_square.append (x**2) 
# print(odd_square)

t1 = (2,4,3,5,6)
print(type(t1))
print(len(t1))
print(3 in t1)
print()

