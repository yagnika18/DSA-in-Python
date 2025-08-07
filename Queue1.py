def enqueue():
    n=int(input("Enter the element to be inserted into Queue:"))
    queue.append(n)
def dequeue():
    if len(queue)==0:
        print("EMPTY")
    else:
        print(queue[0],"is the element deleted from Queue")
        del queue[0]
        print()
def display():
    if len(queue)==0:
        print("EMPTY")
    else:
        print("ELEMENTS IN THE QUEUE ARE:")
        for ele in queue:
            print(ele,end="")
        print("FRONT OF THE QUEUE IS",queue[0])
        print("REAR OF THE QUEUE IS",queue[-1])


queue=list()
while(1):
    print("enter the option below\n1-ENQUEUE OPERATION\n2-DEQUEUE OPEARTION\n3-DISPLAY\nEnter any key to exit")
    str=int(input())
    if str==1:
        print("ENQUEUE OPERATION")
        enqueue()
    elif str==2:
        print("DEQUEU OPERATION")
        dequeue()
    elif str==3:
        print("DISPLAY")
        display()
    else:
        print("EXIT FROM THE PROGRAM")
        break


