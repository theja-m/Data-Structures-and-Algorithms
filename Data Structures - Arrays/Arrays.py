strings = ['a','b','c','d']
# 4*4 = 16 bytes of storage is used

print(strings[2])

#push  
strings.append('e')      # O(1)
#pop  
strings.pop() 
strings.pop()            # O(1)

#addfirstelement 
strings.insert(0,'x')    #O(n)

#splice
strings.insert(2,'alien')   #O(n)

print(strings)

#Array native python methods :-
#append()	Adds an element at the end of the list
#clear()	Removes all the elements from the list
#copy()	Returns a copy of the list
#count()	Returns the number of elements with the specified value
#extend()	Add the elements of a list (or any iterable), to the end of the current list
#index()	Returns the index of the first element with the specified value
#insert()	Adds an element at the specified position
#pop()	Removes the element at the specified position
#remove()	Removes the first item with the specified value
#reverse()	Reverses the order of the list
#sort()	Sorts the list

#List objects are implemented as arrays. 
#They are optimized for fast fixed-length operations and incur O(n) memory movement costs for pop(0) and insert(0, v) 
#operations which change both the size and position of the underlying data representation.

#For in depth information on arrays 
#https://docs.python.org/3/tutorial/datastructures.html

#to implement arrays as a stack 
#https://docs.python.org/3/library/collections.html#collections.deque
In Python, lists are implemented as dynamic arrays, and the time complexity for various operations can be described using Big O notation. Here are the common operations and their time complexities:

# <!-- 1. **Indexing (Accessing an element)**
#    - **Operation**: `list[i]`
#    - **Time Complexity**: O(1)

# 2. **Appending an element**
#    - **Operation**: `list.append(x)`
#    - **Time Complexity**: Amortized O(1)

# 3. **Inserting an element at the end**
#    - **Operation**: `list.insert(len(list), x)`
#    - **Time Complexity**: O(1)

# 4. **Inserting an element at the beginning or middle**
#    - **Operation**: `list.insert(i, x)`
#    - **Time Complexity**: O(n)

# 5. **Deleting an element by index**
#    - **Operation**: `del list[i]`
#    - **Time Complexity**: O(n)

# 6. **Removing an element by value**
#    - **Operation**: `list.remove(x)`
#    - **Time Complexity**: O(n)

# 7. **Popping an element from the end**
#    - **Operation**: `list.pop()`
#    - **Time Complexity**: O(1)

# 8. **Popping an element from the beginning or middle**
#    - **Operation**: `list.pop(i)`
#    - **Time Complexity**: O(n)

# 9. **Concatenation**
#    - **Operation**: `list1 + list2`
#    - **Time Complexity**: O(n + m) where n and m are the lengths of the lists

# 10. **Slicing**
#     - **Operation**: `list[start:end]`
#     - **Time Complexity**: O(k) where k is the length of the slice

# 11. **Checking if an element exists**
#     - **Operation**: `x in list`
#     - **Time Complexity**: O(n)

# 12. **Length of the list**
#     - **Operation**: `len(list)`
#     - **Time Complexity**: O(1)

# 13. **Sorting the list**
#     - **Operation**: `list.sort()`
#     - **Time Complexity**: O(n log n)

# 14. **Reversing the list**
#     - **Operation**: `list.reverse()`
#     - **Time Complexity**: O(n)

# ### Summary
# - **O(1)**: Indexing, appending, popping from the end, checking length.
# - **O(n)**: Inserting/removing elements (not at the end), deleting by index, removing by value, checking if an element exists, reversing.
# - **O(n log n)**: Sorting.
# - **O(n + m)**: Concatenation.
# - **O(k)**: Slicing. -->




