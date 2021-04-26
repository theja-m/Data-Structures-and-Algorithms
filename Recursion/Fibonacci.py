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


def fibonacci(num):
    if num < 2:
        return num
    return fib(num-1) + fib(num-2)


print([fib(i) for i in range(10)])
print([fibonacci(i) for i in range(10)])
print([0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55])
