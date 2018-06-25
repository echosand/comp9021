from binary_tree_adt import *
from math import log


class PriorityQueue(BinaryTree):
    def __init__(self, value = None):
        self.value = value
        self.left_no = 0
        self.right_no = 0
        if self.value is not None:
            self.left_node = PriorityQueue()
            self.right_node = PriorityQueue()
        else:
            self.left_node = None
            self.right_node = None

    def insert(self, value):
        if self.value is None:
            self.value = value
            self.left_node = PriorityQueue()
            self.right_node = PriorityQueue()
        elif self.left_no == 0 and self.right_no == 0:
            # 左侧空插入左侧
            if value <= self.value:
                value,self.value = self.value,value
            self.left_node = PriorityQueue(value)
            self.left_no += 1
        elif self.left_no == 1 and self.right_no == 0:
            # 左侧满了插入右侧
            if value <= self.value:
                value,self.value = self.value,value
            self.right_node = PriorityQueue(value)
            self.right_no += 1
        else:
            if value <= self.value:
                value,self.value = self.value,value
                
            left = (log(self.left_no+1,2)*10)%10
            right = (log(self.right_no+1,2)*10)%10

            if left > 0:
                # should insert into left node
                self.left_node.insert(value)
                self.left_no += 1
            elif right > 0:
                # should insert into right node
                self.right_node.insert(value)
                self.right_no += 1
            elif left == 0 and right == 0:
                if self.left_no > self.right_no:
                    # insert into right
                    self.right_node.insert(value)
                    self.right_no += 1
                else:
                    # start a new level of subnodes from left
                    self.left_node.insert(value)
                    self.left_no += 1
