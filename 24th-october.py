import os

# os.mkdir("Temp Folder")
# print(os.getcwd())
# os.chdir("Temp Folder")
# print(os.getcwd())
# os.chdir("/Users/sourabhyadav/College Code/python")
# print(os.getcwd())
# os.rmdir("Temp Folder")

# f = open("test.txt","w")
# f = open("test.txt","a")
# f = open("test.txt","r")

# f.seek(15) # move the cusor for that file
# print(f.readline())
# offset values : 0 (start), 1 (current), 2 (end) location
# print(f.tell()) # tells the current cursor position , 0 for write , total byte for append

# csv=open("iris-write-from-docker.csv","r")
# print(csv.readlines())

# with open("iris-write-from-docker.csv","r") as csvfile:
#     all_lines = csvfile.readlines()
#     print(all_lines)

# f = open("temp.txt","a")
# i=0
# for i in csv:
#     f.write(csv.readline(i))
#     i+=1
# # file=open("temp.txt","r")
# # print(file.read())


# python exception 
# try, except (catch in js), finally


# try:
#     print("hello",i) # type: ignore
# except NameError:
#     print("Name error , i not defined")
# except Exception as e:
#     print("Error!",e)
# # print("End of program")

# finally: # not related to try or except , it will run after program completes
#     print("End of program")


# try:
#     a=[1,2,3,4]
#     print(a[4])
# except IndexError:
#     print("Out of an index")
# print("End of program")


class MyError(Exception): 
    def __init__(self,msg): 
        self.message=msg 
    def displayError(self): 
        return self.message

try: 
    a=int(input("Enter a: ")) 
    b=int(input("Enter b: ")) 
    if b==0:
        raise MyError("value of b cannot zero") 
    c=a/b
except MyError as e:
    print("Error: ",e.displayError())
except: 
    print("Error occured")
else:
    print("division is: ",c)
finally:
    print("In finally")