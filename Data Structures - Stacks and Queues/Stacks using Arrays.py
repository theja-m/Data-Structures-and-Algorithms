class Stack:
  def __init__(self):
    self.arr = []
    self.length = 0
  
  def __str__(self):
    return str(self.__dict__)
  
  def peek(self):
    return self.arr[self.length-1]

  def push(self,value):
    self.arr.append(value)
    self.length += 1

  def pop(self):
    popped_item = self.arr[self.length-1]
    del self.arr[self.length-1]
    self.length -= 1
    return popped_item

mystack = Stack()
mystack.push('google')
mystack.push('microsoft')
mystack.push('facebook')
mystack.push('apple')
print(mystack)
x = mystack.peek()
print(x)
mystack.pop()
print(mystack)


