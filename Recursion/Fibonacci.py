def fib(num):
    if num < 2:
        return num
    a = 0
    b = 1
    total = 0
    for i in range(num-1):
        total = a+b
        a = b
        b = total
    return total


def fib_2(num):
    """
    Second methon using iteration to generate fibonacci number
    """
    arr = [0, 1]
    for i in range(2, num+1):
        arr.append(arr[i-1]+arr[i-2])
    return arr[num]


def fibonacci(num):
    if num < 2:
        return num
    return fibonacci(num-1) + fibonacci(num-2)


print([fib(i) for i in range(10)])
print([fib_2(i) for i in range(10)])
print([fibonacci(i) for i in range(10)])
print([0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55])
