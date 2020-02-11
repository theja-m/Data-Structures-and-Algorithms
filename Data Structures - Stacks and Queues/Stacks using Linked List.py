class Node:
  def __init__(self,data):
    self.data = data
    self.next = None

class Stack:
  def __init__(self):
    self.top = None
    self.bottom = None
    self.length = 0
  
  def peek(self):
    return self.top.data

  def push(self,data):
    new_node = Node(data)
    if self.bottom == None:
      self.bottom = new_node
      self.top = self.bottom
      self.length = 1
    else:
      self.top.next = new_node
      self.top = self.top.next
      self.length += 1

  def pop(self):
    i = 1
    curr_node = self.bottom
    while i != self.length-1:
      curr_node = curr_node.next
      i+=1
    popped_value = curr_node.next
    curr_node.next = None
    self.top = curr_node
    self.length -= 1
    return popped_value.data

  def printt(self):
    temp = self.bottom
    while temp != None:
      print(temp.data , end = ' -> ')
      temp = temp.next
    print()
mystack = Stack()
mystack.push('google')
mystack.push('microsoft')
mystack.push('facebook')
mystack.push('apple')
mystack.printt()
x = mystack.peek()
print(x)
y=mystack.pop()
print(y)
mystack.printt()
qw = mystack.peek()
print(qw)
