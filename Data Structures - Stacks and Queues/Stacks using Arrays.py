class Stack:
  def __init__(self):
    self.arr = []
    self.length = 0
  
  # return stack 
  def __str__(self):
    return str(self.arr)
  
  # return length of stack
  def size(self):
    return self.length

  # return True if stack is Empty otherwise return False
  def isEmpty(self):
    if self.length==0:
        return True
    else:
        return False
        
  # return top of stack
  def peek(self):
    return self.arr[self.length-1]

  # push value in stack
  def push(self,value):
    self.arr.append(value)
    self.length += 1

  # return top of stack and also remove it from  stack
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
print(mystack.isEmpty())
print(mystack.size())
