# 15 --> 6 --> 8

class Node():

  def __init__(self,data):
    self.data = data
    self.next = None
    
class LinkedList():

  def __init__(self):
    self.head = None
    self.tail = None
    self.length = 0
  
  def append(self,data):
    new_node = Node(data)
    if self.head == None:
      self.head = new_node
      self.tail = self.head
    else:
      self.tail.next = new_node
      self.tail = new_node 
    self.length += 1

  def prepend(self,data):
    new_node = Node(data)
    if self.head == None:
      self.head = new_node
      self.tail = self.head
    else:
      new_node.next = self.head 
      self.head = new_node
    self.length += 1

  def insert(self,index,data):
    if index > self.length:
      self.append(data)
    elif index <= 0:
      self.prepend(data)
    else:
      new_node = Node(data)
      current_node = self.traverse(index)
      temp = current_node.next
      current_node.next = new_node
      new_node.next = temp
      self.length += 1

  def remove(self,index):
    if index >= self.length:
      print("Entered wrong index")
      return None
    elif index <= 0:
      self.head = self.head.next
    else:
      current_node = self.traverse(index)
      current_node.next = current_node.next.next
    self.length -= 1

  def traverse(self,index):
    current_node = self.head
    for i in range(index-1):
      current_node = current_node.next
    return current_node

  def printl(self):
    temp = self.head
    while temp != None:
      print(temp.data , end = ' ')
      temp = temp.next
    print()
    print('Length = '+str(self.length))

  def reverse(self):
    prev = None
    self.tail = self.head 
    while self.head != None:
      temp = self.head
      self.head = self.head.next
      temp.next = prev
      prev = temp  
    self.head = temp
    

l = LinkedList()
l.append(10)
l.append(5)
l.append(6)
l.prepend(1)
l.insert(2,99)
l.insert(34,23)
l.remove(5)
l.reverse()
l.printl()
print(l.head.data, l.tail.data)