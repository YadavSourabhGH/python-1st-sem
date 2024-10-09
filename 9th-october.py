# 9th october
# functions
# with function we can store the code snippet which is used many time in application
# # def means define
# input("prompt {arg}")

# def functionname(parameter):
#     "function_docstring"
#      function_suite
#      return(expression)


# def message():
#     print("Hello!")
# message()
# print(message()) #output : None


# def message_with_return():
#     return "Hello!"
# print(message_with_return())


# def message_with_arg1(msg):
#     print(msg)
# message_with_arg1() #error : TypeError: message_with_arg() missing 1 required positional argument: 'msg'


# def message_with_arg2(msg):
#     print(msg)
# message_with_arg2(input("Give Me Message : "))


# def multiple_args(name,period):
#     print("Hello",name)
#     print("good",period)
# multiple_args("Samendra","night") #1st method
# multiple_args(period="Evening",name="Samual") #2nd method (can be give suffled parameter)


# def multiple_args_with_default_args(name,period="night"):
#     print("Hello",name)
#     print("good",period)
# multiple_args_with_default_args("surenali")




# def sum(*numbers): #variable argument start with *         it receive tupple (1,2,3)
#     s=0
#     for n in numbers:
#         print(s,"+",n,"=",s+n)
#         s+=n
#     print("sum : ",s,numbers)
# # sum(1.93,3.14,3.1)
# sum()



# def sum_with_return(a,b):
#     return a+b
# print(sum_with_return(2,3))



# Write a program accept numbers from user until user wants and then sum and average

# flag = True
# nums=[]
# sum = 0

# while flag == True:
#     num = input("Enter Number (Enter Again To Exit) : ")
#     if num == "":
#         flag=False
#         for i in range(0,len(nums)):
#             sum += int(nums[i])
#         print("Sum :",sum)
#         print("Average :",sum/len(nums))
        
#     else:
#         nums.append(num)
    



# def calc_main(a,b):
#     def add(a,b):
#         return a+b
#     def subtract(a,b):
#         return a-b
#     def div(a,b):
#         return a/b
#     def multi(a,b):
#         return a*b
#     print(
#         f'''
# Sum : {add(a,b)}\n : subtract : {subtract(a,b)}\n Division : {div(a,b)}\nMultiplication : {multi(a,b)}
# '''
#     )

# calc_main(7,8)



def calc_main(a,b):
     def add(a,b):
        return a+b
     def subtract(a,b):
        return a-b
     def div(a,b):
        return a/b
     def multi(a,b):
        return a*b
     return add(a,b),subtract(a,b),div(a,b),multi(a,b)

calc = calc_main(40,10)
print(f'Sum : {calc[0]}\nSubtract : {calc[1]}\n multiplication : {calc[3]}\n division : {calc[2]}')