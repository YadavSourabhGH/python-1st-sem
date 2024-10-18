# # set - unorder - dont have indexing 
# # list - tupple - have index
# # list - tubble - allowed to enter diff type of element 
# # in set we cant reapeat the element
# # [] - list 
# # () - tupple
# # {} - dict
# # set() - set

# s=set()
# s={1,2,3,4,5}
# print(type(s))
# s2=set()
# s2={8,4,5,3,2,6,4}
# s.add(1)
# print(s)
# s.clear()
# s.copy()
# s.difference(s2)
# s.intersection()
# # s.isdisjoint()
# # s.issubset()
# # s.issuperset()
# # s.pop()
# # s.remove()
# # s.symmetric_difference()
# # s.union()
# # s.update()
# print(s.issubset(s2))



#make a program for a group and add functions to add ,view and remove memeber in the group 
sname = set()
sname={"admin(You)"}
def main():
    print("\tMain Menu\n","-"*30,"\n\t1. view member\n\t2. add member\n\t3. remove member")
    option=int(input("Select a option : "))
    if(option==1):
        print("-"*25)
        print("Users")
        for i in sname:
            print(i)
        main()
    elif(option==2):
        iname=input("Enter new User Name : ")
        if iname:
            if iname in sname:
                print("User already in group")
                main()
            else:
                sname.add(iname)
                print(iname,"Added")
                main()
    elif(option==3):
        rname=input("Enter Username to remove from group : ")
        if rname:
            if rname not in sname:
                print("No User Found")
                main()
            else:
                sname.remove(rname)
                print(rname,"Removed")
                main()
                
main()