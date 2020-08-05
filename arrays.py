# author: Pratyusha

# array is a list of homogenous elements. It is a linear data structure
# we are creating an array on top of inbuilt datastructure 'lists' in python
# so we can make use of most of its methods
# By default, the array type == int, it can be changed to any other datatype
# The following operations are performed on MyArray:
#         1. insert an element:
#             - push(item) : inserts at end of array
#             - push(item,index) : inserts at particular index
        # 2. delete an element:
        #     - pop() : delete last element of array
        #     - pop(index) : delete element at the particular index
        # 3. search an element(by index):
        #     - get(index): print the element at particular index
        # 4. traverse:
        #     - traverse() : print elements of array
        # 5. update an element:
        #     - update(item,index) : changes the element at the particular index

class MyArray(object):
    # creates a new list for array
    # specify the type of elements the array will hold
    def __init__(self,type=int):
        self._items=[]
        self.type = type

    # add items to MyArray
    def push(self,item,index=None):
        if type(item)== self.type:
            if index == None : # insert element to end of MyArray
                self._items.insert(len(self._items),item) #same as self._items.append(item)
                #print(self._items)
            else: #insert elements at particular index
                self._items.insert(index,item)
                print(self._items)
        else:
            print('The element is not of {} datatype'.format(self.type))


    # delete elements from array
    def pop(self,index=None):
        if index == None: # delete element from the end of the MyArray
            self._items.pop()
            print(self._items) #returns the elements present in the array after pop
        else: # delete element at the particular index from the MyArray
            del self._items[index]
            print(self._items) #returns elements after delete operation

    # to get an element at a particular index
    def get(self,index):
        print(self._items[index])

    # traversing: print all elements of array
    def traverse(self):
        print(self._items) #returns all elements of MyArray

    # update an element in array
    def update(self,item,index):
        if type(item)== self.type:
            self._items[index] = item
            print(self._items)
        else:
            print('The element is not of {} datatype'.format(self.type))

# create an object for the MyArray class
if __name__ == '__main__':
    a = MyArray(int)
    a.push(10)
    a.push(20)
    a.push(30)
    a.push(40)
    a.push(50)
    a.push(60)
    a.traverse()
    a.push(70)
    a.push(80)
    a.push(90,6)
    a.update(50,0)
    # a.update('hey',1) #the else part gets printed
    # a.delete(3)
    # a.push('hello') #the else part gets printed
    # a.pop()
