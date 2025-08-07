def push():
    n=int(input("Enter the element to be inserted into stack:"))
    if len(stack)==0:
        stack.append(n)
    else:
        stack.insert(0,n)
    print(n,"is inserted into stack")

def pop():
    if len(stack)==0:
        print("Stack is empty")
    else:
        print(stack[0],"is deleted from stack")
        del stack[0]
        
def display():
    if len(stack)==0:
        print("EMPTY STACK")
    else:
        print("Elements of stack are:")
        for ele in stack:
            print(ele)
        print("Top of the stack is",stack[0])     


stack=list()
while(1):
    print("enter the option below\n1-PUSH OPERATION\n2-POP OPEARTION\n3-DISPLAY\nEnter any key to exit")
    str=input()
    if str=='1':
        print("PUSH OPERATION")
        push()
    elif str=="2":
        print("POP OPEARTION")
        pop()
    elif str=="3":
        print("DISPLAY FUNCTION")
        display()
    else:
        print("EXIT FROM PROGRAM")
        break
        