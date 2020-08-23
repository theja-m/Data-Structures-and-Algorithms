def func(mylist):

  for i in range(0,len(mylist)):
    for j in range(i+1,len(mylist)):
      if mylist[i] == mylist[j]:
        return mylist[i] 
  return 0


def hashtable(mylist):
  mydict = {}
  for i in range(len(mylist)):
    if mylist[i] in mydict:
      return mylist[i]
    else:
      mydict[mylist[i]]=i
  return 0
  
# Exercise:
# Iterative funtion to return the same result
# as the hashtable function
def func2(mylist):

  for i in range(len(mylist)):
    temp = []
    for j in range(i+1,len(mylist)):
      if mylist[j] in temp:
        return mylist[j]
      else:
        temp.append(mylist[j])
      if mylist[i] == mylist[j]:
        return mylist[i] 
  return 0

mylist = [2,1,1,2,3,4,5]
x = func(mylist)
print(x)
y = hashtable(mylist)
print(y)
z = func2(mylist)
print(z)