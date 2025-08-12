class Node:
    def __init__(self,x):
        self.data=x
        self.next=None
class Stack:
    def __init__(self):
        self.top=None
    def push(self):
        x=int(input("Enter the element to be inserted:"))
        new=Node(x)
        if self.top is None:
            self.top=new
            self.top.next=None
        else:
            new.next=self.top
            self.top=new
    def pop(self):
        if self.top is None:
            print("Stack is empty")
        elif self.top.next is None:
            print("Popped Element is:",self.top.data)
            print("-----------------------")
            self.top=None
        else:
            temp=self.top
            print("Popped Element is:",self.top.data)
            print("-----------------------")
            self.top=temp.next
            temp=None
    def display(self):
        if self.top is None:
            print("Stack is Empty")
            print("--------------------")
        else:
            print("The elements in the stack are:")
            temp=self.top
            while temp:
                print(temp.data)
                temp=temp.next
            print("TOP OF THE STACK:",self.top.data)
            print("---------------------")
s=Stack()
while(1):
    print("Enter the options below:")
    print("1-Push Operation\n2-Pop operation\n3-Display\n4-Exit")
    option=int(input())
    if option==1:
        print("Push Operation")
        s.push()
    elif option==2:
        print("Pop OPeration")
        s.pop()
    elif option==3:
        print("Display")
        s.display()
    else:
        print("Exit from the program")
        break