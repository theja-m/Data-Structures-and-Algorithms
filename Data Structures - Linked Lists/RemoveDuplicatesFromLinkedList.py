# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None
    
    def addMany(self, values):
        current = self
        while current.next is not None:
            current = current.next
        for value in values:
            current.next = LinkedList(value)
            current = current.next
        return self
    
    def getNodesInArray(self):
        nodes = []
        current = self
        while current is not None:
            nodes.append(current.value)
            current = current.next
        return nodes

def removeDuplicatesFromLinkedList(linkedList):
  
    slowptr = linkedList
    while slowptr.next is not None:
        if slowptr.value == slowptr.next.value:
            slowptr.next = slowptr.next.next
        else:
            slowptr = slowptr.next
    return linkedList
    


llist = LinkedList(1)

llist.addMany([1, 3, 4, 4, 4, 5, 6, 6])
print(llist.getNodesInArray())

removeDuplicatesFromLinkedList(llist)
print(llist.getNodesInArray())


# O(n) -> time
# O(1) -> space        



  # Write your code here.
    # # [1, 1, 3, 4, 4, 4, 5, 6, 6]
    
    # if len(linkedList.getNodesInArray()) > 1:
