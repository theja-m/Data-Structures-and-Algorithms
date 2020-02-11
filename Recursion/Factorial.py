def factorial(num):
  if num == 1:
    return 1
  return num * factorial(num-1)

def fact(num):
  result = 1
  for i in range(1,num+1):
    result = result * i
  return result

print(fact(6))
  
print(factorial(4))