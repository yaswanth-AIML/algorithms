class node:
    def __init__(self,val):
        self.val=val
        self.next=None
class Linked_list():
    def __init__(self):
        self.head=None
    def insert(self,val):
        new=node(val)
        if self.head==None:
            self.head=new
        else:
            curr=self.head
            while curr.next!=None:
                curr=curr.next
            curr.next=new
        return self.traverse()
    def insert_at_first(self,val):
        new=node(val)
        if self.head==None:
            self.head=new            
        else:
            temp=self.head
            self.head=new
            self.head.next=temp
        return self.traverse()
    def insert_at_pos(self,val,index):
        new=node(val)
        if self.head==None and index==0:
            self.head=new
            return self.traverse()
        l=0
        curr=self.head
        while curr!=None:
            l=l+1
            curr=curr.next
        if index>l-1:
            print("index out of range")
        else:
            if index == 0:
                new.next = self.head
                self.head = new
                return self.traverse()
            curr=self.head
            for i in range(index-1):
                curr=curr.next
            new.next=curr.next
            curr.next=new
            return self.traverse()
    def delete_at_first(self):
        curr=self.head
        if self.head==None:
            print("can't delete from empty linked list")
        elif curr.next==None:
            self.head=None
            print("deleted the head linked list is empty")
            return
        else:
            self.head=curr.next
            return self.traverse()
    def delete(self):
        curr=self.head
        if self.head==None:
            print('cant delete if empty')
            return []
        elif self.head.next==None:
            self.head=None
            print("deleted")
            return []
        else:
            while curr.next.next!=None:
                curr=curr.next
            curr.next=None
            return self.traverse()
    def delete_at_pos(self,index):
            if self.head==None:
                print("cant delete from empty linked list")
                return self.traverse()
            elif index==0:
                self.head =self.head.next
                return self.traverse()   
            else:
                l=0
                curr=self.head    
                while curr!=None:
                    l+=1
                    curr=curr.next
                if index>=l:
                    print("index out of range")
                    return self.traverse()
                else:
                    curr=self.head
                    for i in range(index-1):
                        curr=curr.next
                    curr.next=curr.next.next
                    return self.traverse()
    def traverse(self):
        if self.head==None:
            print("empty linked list")
            return []
        else:
            curr=self.head
            while curr!=None:
                print(curr.val,"->",end=" ")
                curr=curr.next
            print(None)
s1 = Linked_list()
while True:
    print("""
    Choose operation:
    1. Insert at end
    2. Insert at beginning
    3. Insert at position
    4. Delete at beginning
    5. Delete at end
    6. Delete at position
    7. Traverse
    8. Exit
    """)
    try:
        choice=int(input("enter a operation: "))
    except:
        print("ENTER THE CORRECT ONE")
        choice=int(input("enter a operation "))
    else:
        if choice==1:
            num=int(input("enter the number to insert at end:"))
            s1.insert(num)
        elif choice==2:
            num=int(input("enter the number to insert at beginning:"))
            s1.insert_at_first(num)
        elif choice==3:
            num=int(input("enter the number to insert:"))
            index=int(input("enter the index number to insert the number:"))
            s1.insert_at_pos(num,index)
        elif choice==4:
            s1.delete_at_first()
        elif choice==5:
            s1.delete()
        elif choice==6:
            index=int(input("enter on which position do youb wanna delete the number 0 based index:"))
            s1.delete_at_pos(index)
        elif choice==7:
            s1.traverse()
        elif choice==8:
            break
        else:
            print("'ENTER THE CORRECT OPERATION'")
