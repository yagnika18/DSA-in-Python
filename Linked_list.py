class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class Singlylinkedlist:
    def __init__(self):
        self.head=None

    def insert_beginning(self,data):
        new_node=Node(data)
        new_node.next=self.head
        self.head=new_node
    

    def insert_end(self,data):
        node_end=Node(data)
        temp=self.head
        while temp.next:
            temp=temp.next
        temp.next=node_end

    def insert_position(self,pos,data):
        np=Node(data)
        temp=self.head
        for i in range(pos-1):
            temp=temp.next
        np.data=data
        np.next=temp.next
        temp.next=np
    def delete_beginning(self):
        temp=self.head
        self.head=temp.next
        temp.next=None
    def delete_end(self):
        prev=self.head
        temp=self.head.next
        while temp.next is not None:
            temp=temp.next
            prev=prev.next
        prev.next=None
    def delete_position(self,pos):
        prev=self.head
        temp=self.head.next
        for i in range(1,pos-1):
            temp=temp.next
            prev=prev.next
        prev.next==temp.next
    def display(self):
        if self.head is None:
            print("Linkedlist is empty")
        else:
            temp=self.head
            while temp:
                print(temp.data,"-->",end=" ")
                temp=temp.next

L=Singlylinkedlist()
n=Node(10)
L.head=n
n1=Node(20)
L.head.next=n1
n2=Node(30)
n1.next=n2
L.insert_beginning(5)
L.insert_end(40)
L.insert_position(2,15)
#L.delete_beginning()
#L.delete_end()
L.delete_position(2)
L.display()