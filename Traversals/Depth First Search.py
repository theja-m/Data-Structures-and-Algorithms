class Node:
  def __init__(self,val):
    self.val = val
    self.left = None
    self.right = None

class BinarySearchTree:
  def __init__(self):
    self.root = None
  
  def insert(self,val):
    new_node = Node(val)
    if self.root == None:
      self.root = new_node
      return 
    temp = self.root
    while True:
      if new_node.val < temp.val:
        if temp.left == None:
          temp.left = new_node
          break
        else:
          temp = temp.left
      elif new_node.val > temp.val:
        if temp.right == None:
          temp.right = new_node
          break
        else:
          temp = temp.right

  def lookup(self,val):
    temp = self.root
    while True:
      if temp.val == val:
        return True
      elif temp == None:
        return False
      elif val < temp.val:
        temp = temp.left
      elif val > temp.val:
        temp = temp.right

  def inorder(self,currnode,mylist):
    if currnode != None:
      self.inorder(currnode.left,mylist)
      mylist.append(currnode.val)
      self.inorder(currnode.right,mylist)
    return mylist

  def preorder(self,currnode,mylist):
    if currnode!=None:
      mylist.append(currnode.val)
      self.preorder(currnode.left,mylist)
      self.preorder(currnode.right,mylist)
    return mylist

#According to Andre's video , below is easily understandable

  def postorder(self,currnode,mylist):
    if currnode.left:
      self.postorder(currnode.left,mylist)
    if currnode.right:
      self.postorder(currnode.right,mylist)
    mylist.append(currnode.val)
    return mylist
    
      
    

tree = BinarySearchTree()
tree.insert(9)
tree.insert(4)
tree.insert(6)
tree.insert(20)
tree.insert(170)
tree.insert(15)
tree.insert(1)
print(tree.inorder(tree.root,[]))
print(tree.preorder(tree.root,[]))
print(tree.postorder(tree.root,[]))

