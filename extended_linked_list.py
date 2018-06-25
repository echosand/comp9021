from linked_list_adt import *

class ExtendedLinkedList(LinkedList):
    def __init__(self, L = None):
        super().__init__(L)

class ExtendedLinkedList(LinkedList):
    def __init__(self, L = None):
        super().__init__(L)

class ExtendedLinkedList(LinkedList):
    def __init__(self, L = None):
        super().__init__(L)

class ExtendedLinkedList(LinkedList):
    def __init__(self, L = None):
        super().__init__(L)

    def rearrange(self):
        if len(self)<=2:
            return
        else:
            times=len(self)//2-1
        minvalue=self.head.value
        node=self.head
        while node:
            if minvalue > node.value:
                minvalue = node.value
            node=node.next_node
        ad0=self.head
        node=self.head
        while node.next_node:
            node=node.next_node
        node.next_node=ad0
        node = self.head
        while node.next_node.next_node.value!=minvalue:
            node=node.next_node
        self.head=node.next_node
        node.next_node=None

        pre=self.head
        current= self.head.next_node
        self.head=current
        temp=current.next_node
        current.next_node=pre
        pre.next_node=temp.next_node

        while temp.next_node and temp.next_node.next_node :
            current=temp.next_node
            pre=temp
            temp=temp.next_node.next_node
            current.next_node=pre
            pre.next_node=temp.next_node
        pre.next_node.next_node=temp
        temp.next_node=None
