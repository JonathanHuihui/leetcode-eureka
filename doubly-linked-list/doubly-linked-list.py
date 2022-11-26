#!/usr/bin/env python3

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class List:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
    
    def _initcheck(self, new):
        # method to check if it is a new list 
        # or not, not implemented yet
        return NotImplementedError

    def _return_node(self, index):
        node = self.head
        i = 0
        while i < index:    
            node = node.next
            i += 1
        return node

    def printlist(self):
        node = self.head
        while node.next is not None:
            print(node.value)
            node = node.next
        # print the last value
        print(self.tail.value)

    def reverseprint(self):
        node = self.tail
        while node.prev is not None:
            print(node.value)
            node = node.prev
        # print the head value
        print(self.head.value)

    def append(self, value):
        new = Node(value)
        if self.head is None:
            self.head = new
            self.tail = new
        else:
            new.prev = self.tail
            self.tail.next = new
            self.tail = new
        self.length += 1

    def prepend(self, value):
        new = Node(value)
        if self.head is None:
            self.head = new
            self.tail = new
        else: 
            new.next = self.head # set the new node to point to head
            self.head.prev = new
            self.head = new # head is now new node
        self.length+=1

    def insert(self, index, value):
        new = Node(value)
        if self.head is None:
            self.head = new
            self.tail = new
        elif index == 0:
            self.prepend(value)
        elif index >= self.length:
            self.append(value)
        else:
            lead = self._return_node(index-1) # get node before insert
            rlead = self._return_node(index)  # get node at insert

            new.next = lead.next # set new nodes next to the next node
            lead.next = new # set node at 1 next to new node

            new.prev = lead # set new node to point to lead as prev
            rlead.prev = new # set node to point to new node as prev

            self.length += 1

    def remove(self, index):
        if index >= self.length:
            print("Index does not exist. ")
            #print(f'Reference: list is {self.length} elements long')
        elif self.head is None:
            print("This list has not been initialized.")
        elif index == 0:
            lead = self.head.next
            self.head = lead
            self.length -= 1
        else:
            lead = self._return_node(index-1) # get node before bad node
            rlead = self._return_node(index+1) # get node after bad node
            old = lead.next # find the next node
            lead.next = old.next # store that node instead
            rlead.prev = lead # 
            self.length -= 1


linked_list = List()
linked_list.append(value=1)
linked_list.append(value=3)
linked_list.append(value=5)
linked_list.append(value=9)
linked_list.append(value=7)
linked_list.prepend(value=0)
linked_list.insert(2,2)
linked_list.remove(index=5)
linked_list.reverseprint()
print('')
linked_list.printlist()

