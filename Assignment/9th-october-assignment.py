import array as arr

# # Q1. Write a Python program to reverse the order of the items in the array.

# array1 = arr.array('i',[2, 4, 6, 3, 8, 7, 9, 1])
# reversed_array=arr.array('i',[])
# for i in range(1,len(array1)+1):
#     reversed_array.append(array1[-i])
# print(reversed_array)




# # 2. Write a Python program to get the number of occurrences of a specified element in an array.

# array2 = arr.array('i',[])
# a = input("Enter All Number Values (Eg: 5 3 7 5) : ").split(" ")
# for i in range(0,len(a)):
#     array2.append(int(a[i]))
# e = int(input("Enter the number of which you would like to find occarance : "))
# occ = 0
# index = []
# for i in range(0,len(array2)):
#     if array2[i] == e:
#         occ+=1
#         index.append(i)
# print(f'The Element {e} is occured {occ} times at index(s) {index}')




# # 3. Write a Python program to find out if a given array of integers contains any duplicate elements.

# array3 = arr.array('i', [])
# a = input("Enter All Number Values (Eg: 5 3 7 5) : ").split(" ")
# for i in range(0, len(a)):
#     array3.append(int(a[i]))

# duplicates = False
# checked = set()

# for num in array3:
#     if num in checked:
#         print("Yes the array contains duplicates!")
#         duplicates = True
#         break
#     checked.add(num)

# if not duplicates:
#     print("No the array does not contain duplicates.")




# # 4. Write a  Python program to find the missing number in a given array of 5 continuous numbers.

# array4 = arr.array('i', [])
# a = input("Enter All Number Values (Eg: 1 2 . . .) : ").split(" ")

# for i in range(0, len(a)):
#     array4.append(int(a[i]))
# missing_number = None

# for i in range(1, len(array4)):
#     if array4[i] != array4[i - 1] + 1:
#         missing_number = array4[i - 1] + 1
#         break

# if missing_number is None:
#     print("The numbers are in continuous order.")
# else:
#     print("The numbers are NOT in continuous order.")
#     print(f"Missing Number: {missing_number}")




# # 5. Replace all odd numbers in the given array with -1

# array5 = arr.array('i', [])
# a = input("Enter All Number Values (Eg: 1 4 . . .) : ").strip().split(" ")

# for i in range(0, len(a)):
#     array5.append(int(a[i]))
# for i in range(0,len(array5)):
#     if array5[i] % 2 != 0:
#         array5[i]=-1
# print(array5)