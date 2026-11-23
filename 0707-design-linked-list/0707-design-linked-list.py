class Node:
    def __init__(self,val):
        self.val=val
        self.next=None

class MyLinkedList(object):
    def __init__(self):
        self.head=None
    
    def get(self, index):
        temp=self.head
        count=0
        while temp:
            if count == index:
                return temp.val
            temp=temp.next
            count+=1
        return -1

        """
        :type index: int
        :rtype: int
        """
        

    def addAtHead(self, val):
        new_node=Node(val)
        new_node.next=self.head
        self.head=new_node
         
        """
        :type val: int
        :rtype: None
        """
        

    def addAtTail(self, val):
        new_node=Node(val)
        if self.head is None:
            self.head=new_node
            return
        temp=self.head
        while temp.next:
            temp=temp.next
        temp.next=new_node

        """
        :type val: int
        :rtype: None
        """
        

    def addAtIndex(self, index, val):
        if index==0:
            self.addAtHead(val)
            return
        temp=self.head
        count=0
        while temp and count<index-1:
            temp=temp.next
            count+=1
        if temp is None:
            return
        new_node=Node(val)
        new_node.next=temp.next
        temp.next=new_node

    def deleteAtIndex(self, index):
    
        if self.head and None:
            return
        if index==0:
            self.head=self.head.next
            return
        temp=self.head
        count=0
        while temp.next and count<index-1:
            temp=temp.next
            count+=1
        if temp.next:
            temp.next=temp.next.next
        
# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)