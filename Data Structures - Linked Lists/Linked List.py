# 15 --> 6 --> 8

class Node():

  def __init__(self,data):
    self.data = data
    self.next = None
    
class LinkedList():

  def __init__(self):
    self.head = None
    self.tail = None
  
  def append(self,data):
    new_node = Node(data)
    if self.head == None:
      self.head = new_node
      self.tail = self.head
      self.length = 1
    else:
      self.tail.next = new_node
      self.tail = new_node 
      self.length += 1

  def prepend(self,data):
    new_node = Node(data)
    new_node.next = self.head 
    self.head = new_node
    

    self.length += 1

  def insert(self,index,data):
    new_node = Node(data)
    i = 0
    temp = self.head
    if index>=self.length:
      self.append(data)
      return 
    while i<self.length:
      if i == index-1:
        temp.next , new_node.next = new_node , temp.next
        self.length+=1
        break
      temp = temp.next
      i+=1
    

  def remove(self,index):
    temp = self.head
    i=0
    while i<self.length:
      if index == 0:
        self.head = temp.next
        self.length -= 1   
        break       
      if i == self.length-1:
        temp.next = None
        self.tail = temp
        self.length -= 1
        break 
      if i == index-1:
        temp.next = temp.next.next
        self.length-=1
        break
      i+=1
      temp = temp.next
    
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
#l.remove(4)
l.reverse()
l.printl()
