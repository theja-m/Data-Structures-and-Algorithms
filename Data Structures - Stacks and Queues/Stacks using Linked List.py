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
      new_node.next = self.top
      self.top = new_node
      self.length += 1
      # print("top:",self.top.data,"top next:",self.top.next.data)

  def pop(self):
    if not self.top:
      return None
    holderPointer = self.top
    self.top = self.top.next
    self.length -= 1
    if self.length==0:
      self.bottom = None
    return holderPointer.data

  def printt(self):
    temp = self.top
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
