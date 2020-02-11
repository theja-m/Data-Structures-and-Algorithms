def reverse(stri):
  mylist=[]
  for i in range(len(stri)-1,-1,-1):
    mylist.append(stri[i])
  return ''.join(mylist)

x=reverse('I am theja')
print(x)  

# or just stri[::-1]