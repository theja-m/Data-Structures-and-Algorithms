def swap(arr, l, r):
    arr[l], arr[r] = arr[r], arr[l]


class Heap(object):
    def __init__(self, arr):
        self.arr = arr
        self.n = len(arr)
        self.createHeap()
        
    def createHeap(self):
        for i in range(self.n // 2 , -1, -1):
            self.heapify(i)
        
    def heapify(self, i):
        while i < self.n // 2:
            l = i * 2 + 1
            r = i * 2 + 2

            largest = i 

            if r < self.n and self.arr[largest] < self.arr[r]:
                largest = r
            if self.arr[largest] < self.arr[l]:
                largest = l 

            if largest == i:
                break 

            swap(self.arr, largest, i)
            i = largest

    def heapsort(self):
        while self.n > 0:
            self.heapify(0)
            swap(self.arr, 0, self.n - 1)
            self.n -= 1

    def __str__(self): 
        return str(self.arr)


arr = [5, 1, 9, 7, 6, 8, 4, 3, 2, 0]

arr = Heap(arr)
arr.heapsort()

print(arr)