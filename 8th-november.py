
from tkinter import *
'''
import tkinter

top = tkinter.Tk()
top.mainloop()




from tkinter import *
root = Tk()
w = Label(root, text='B.Tech CSE', fg='red', bg='white')
w2 = Label(root, text='BTech CSE', fg='red')
w.pack()
w2.pack()

root.mainloop()





top = Tk()
L1 = Label(top, text="User Name")
L1.pack(side = LEFT)
E1 = Entry(top, bd =5)
E1.pack(side = RIGHT)
top.mainloop()



top = Tk()
def getCheckValue():
    print(CheckVar1.get())
    if CheckVar1.get() == 1:
        w = Label(top, text='Tick', fg='red', bg='white')
        w.pack()
    else:
        w = Label(top, text='Untick', fg='red', bg='white')
        w.pack()

        


CheckVar1 = IntVar()
CheckVar2 = IntVar()
C1=Checkbutton(top, text="Music", variable = CheckVar1,onvalue=1,offvalue=0,height=5,width=20,command=getCheckValue)
C2=Checkbutton(top, text="Music", variable = CheckVar2,onvalue=1,offvalue=0,height=5,width=20)
C1.pack()
C2.pack()

top.mainloop()
'''

'''
from tkinter import messagebox

root = Tk()
root.geometry("300x200")
n1=0
n2=0
res=0
opr="+"

def calculate():
    try:
       n1=float(E1.get())
       n2=float(E3.get())
       opr=str(E2.get())
       if opr == "+":
           res = n1+n2
       elif opr == "-":
           res = n1-n2
       elif opr == "*":
           res = n1*n2
       elif opr == "/":
           res = n1/n2
       messagebox.showinfo("",f'{res}')
    except ValueError:
        messagebox.showinfo("","Error in values")
    except UnboundLocalError:
         messagebox.showinfo("","Error in Oprator value")
        

E1 = Entry(root)
E1.pack()
E1.insert(0,"Enter 1st No.")
E1.bind("<FocusIn>",lambda event: E1.delete(0,"end") if E1.get() == "Enter 1st No." else None)
E1.bind("<FocusOut>",lambda event: E1.insert(0,"Enter 1st No.") if E1.get() == "" else None)

E2 = Entry(root)
E2.pack()
E2.insert(0,"Enter Oprator (+, -, *, /)")
E2.bind("<FocusIn>",lambda event: E2.delete(0,"end") if E2.get() == "Enter Oprator (+, -, *, /)" else None)
E2.bind("<FocusOut>",lambda event: E2.insert(0,"Enter Oprator (+, -, *, /)") if E2.get() == "" else None)

E3 = Entry(root)
E3.pack()
E3.insert(0,"Enter 2nd No.")
E3.bind("<FocusIn>",lambda event: E3.delete(0,"end") if E3.get() == "Enter 2nd No." else None)
E3.bind("<FocusOut>",lambda event: E3.insert(0,"Enter 2nd No.") if E3.get() == "" else None)

B1= Button(root, text = "Answer", command = calculate) 
B1.pack()

root.mainloop()
'''




