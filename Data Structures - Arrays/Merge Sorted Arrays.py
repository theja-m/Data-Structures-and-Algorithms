#def mergesortedarr(a,b):
#  x=a+b
#  x.sort()
#  return x

#a=[1,2,3,4]
#b=[3,7,9,12]
#qw=mergesortedarr(a,b)
#print(qw)

#In interview we must solve only like this

def mergesortedarr(a,b):
  if len(a)==0 or len(b)==0:
    return a+b
  mylist=[]
  i=0
  j=0
  while i<len(a) and j<len(b):

    if a[i]<=b[j]:
      mylist.append(a[i])
      i+=1

    elif b[j]<a[i]:
      mylist.append(b[j])
      j+=1

  return mylist+a[i:]+b[j:]

a=[1,3,4,6,20]
b=[2,3,4,5,6,9,11,76]
x=mergesortedarr(a,b)
print(x)


