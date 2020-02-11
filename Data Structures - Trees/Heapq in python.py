import heapq
x = [5,2,8,1,6,7,4,9]
#Heapify method sorts the list , this is min heap  
heapq.heapify(x)
print(x)
heapq.heappush(x,0)
print(x)
print(heapq.heappop(x))
print(x)
# Used to pop and push the element in same time
print (heapq.heappushpop(x, 5)) 
print(x)
#Used to get n largest elements in heap 
print(heapq.nlargest(4,x))
#Used to get n smallest elements in heap
print(heapq.nsmallest(4,x))
