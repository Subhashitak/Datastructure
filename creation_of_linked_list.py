class node:
    def __init__(self,data):
        self.data=data
        self.next=None
class linked_list:
    def __init__(self,head,temp):
        self.head=None
        self.temp=None
    def create(self):
        size=int(input())
        for i in range(size):
            value=int(input())
            newnode=node(value)
            newnode.next=None
            if self.head is None:
                self.head=newnode
                self.temp=newnode
            else:
                self.temp.next=newnode
                self.temp=newnode
    def insertion_at_beginning(self):
        value=int(input())
        newnode=node(value)
        newnode.next=self.head
        self.head=newnode
    def insertion_at_middle(self):
        value=int(input("Enter the data: "))
        newnode=node(value)
        pos=int(input("Enter the position: "))
        self.temp=self.head
        i=1
        while i<pos:
            self.temp=self.temp.next
            i=i+1
        newnode.next=self.temp.next
        self.temp.next=newnode
        

    def insertion_at_end(self):
        value=int(input())
        newnode=node(value)
        self.temp=self.head
        while self.temp.next is not None:
            self.temp=self.temp.next
        self.temp.next=newnode
    def deletion_at_beginnig(self):
        self.temp=self.head
        self.head=self.head.next
        self.temp.next=None
        del self.temp
    def deletion_at_position(self):
        self.temp=self.head.next
        prev=self.head
        for i in range(1,pos-1):
            prev=prev.next
            self.temp=self.temp.next
        prev.next=self.temp.next
        del self.temp  
        
    def deletion_at_end(self):
        self.temp=self.head.next
        prev=self.head
        while self.temp.next is not None:
            prev=prev.next
            self.temp=self.temp.next
        prev.next=None
    def display(self):
        self.temp=self.head
        while self.temp is not None:
            print(self.temp.data)
            self.temp=self.temp.next
ll=linked_list(None, None)
ll.create()
ll.display()
ll.insertion_at_beginning()
ll.display()
ll.insertion_at_end()
ll.display()
ll.insertion_at_middle()
ll.display()
ll.deletion_at_beginnig()
ll.display()
ll.deletion_at_end()
ll.display()
