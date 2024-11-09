# 1. WAP to find the number of words in the given text file
'''
text = input("Enter the text: ").split()
if(text):
    count=0
    for i in range(len(text)):
        if text[i]!=" " or None:
            count+=1
    print(f'No. of words in given string are : {count}')
else:
    print("Invalid Input")
'''




# 2. Write a program to write “Happy Programming” in a text file and read it
'''
test_file = open('test.txt','w')
test_file.write("Happy Programming")
test_file.close()
test_file = open('test.txt','r')
print(test_file.read())
'''




# 3. WAP to demonstrate the working of the following functions:
#           i) read()
#           ii) read(n)
#           iii) readline()
#           iv) readlines()
'''
read_file = open("read_file_test.txt","w")
read_file.write("Hello World\nWelcome to python\nReady")
'''
# now file have data:
'''
Hello World
Welcome to python
Ready
'''
'''
read_file.close()
read_file = open("read_file_test.txt","r")

print(read_file.read())
'''
# output:
'''
Hello World
Welcome to python
Ready
'''
'''
read_file.seek(0) 
# using seek because we used read above so after
# that the pointer goes to last place , doing seek(0) bring back the pointer to 0

print(read_file.read(10)) # for testing we provided 10 as size in byte(s)
'''
# output:
'''
Hello Worl
'''
'''
read_file.seek(0) 

print(read_file.readline()) # print 1st line : Hello World
print(read_file.readline()) # print 2nd line : Welcome to python
print(read_file.readline()) # print 3rd line : Ready
'''
#each readline() printing each line is because of 
# in 1st read_file.readline() the pointer of the file goes to end of that line and print single line 
# similarly in 2nd read_file.readline()) it print 2nd after that the pointer of that file goes to end of 2nd 
#and at last it print 3rd line
'''
read_file.seek(0) 
print(read_file.readlines()) # return list which contains all lines as a list element
'''
# output:
'''
['Hello World\n', 'Welcome to python\n', 'Ready']
'''




# 4. WAP that exhibits the working of the following functions:
#           i. write()
#           ii. writelines()

# write_file = open("write_file_test.txt","w")
# write_file.write("Hello world")
# lines = ["hello world\n", "this is python\n", "welcome to py"]
# write_file.writelines(lines)
# write_file.close()