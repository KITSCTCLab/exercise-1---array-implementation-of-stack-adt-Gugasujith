import os
class Stack:
    def __init__(s,n):
        s.n= n
        s.st=[None]*n
        s.top = -1

    def push(s):
       if s.top == s.n-1:
            print("Stack full!")
       else:
            s.top += 1
            data = int(input("Data to be pushed: "))
            s.st[s.top] = data

    def pop(s):
      if s.top == -1:
            print("Empty stack")
       else:
            s.top = s.top-1
            data = s.st[s.top]
            return data
     
    def peek(s):
       print(s.st[s.top])
        

    def display(self):
        for i in range(s.top + 1):
            print(s.st[i],end=",")

n = int(input("Enter the size of integer: "))
s1 = stackADT(n)

while(1):
    print("\n***SPECIFY BY THE FUNCTIONS BY NUMBERS***")
    print("\n 1.Push \n 2.Pop \n 3.Peek \n 4.Display \n 5.EXIT")
    ch = int(input("Function to be performed: "))
    
    if ch == 1:
        print("Inserted")
        s1.push()
    elif ch == 2:
        print("Deleted")
        s1.pop()
    elif ch == 3:
        print("Top element dislay")
        s1.peek()
    elif ch==4:
        ("Total list display")
        s1.display()
    else:
        print("Thank you , have a nice day!")
        break
