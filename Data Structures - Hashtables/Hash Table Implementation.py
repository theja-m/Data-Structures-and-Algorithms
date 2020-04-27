class Hashmap():
     def __init__(self):
          self.size=50
          self.map=[None]*self.size

     def _gethash(self,key):
          h=0
          for char in str(key):
               h+=ord(char)
          return h % self.size
     def set(self,key,value):
          address=self._gethash(key) 
          if self.map[address]==None:
               self.map[address]=[]
          self.map[address].append([key,value])     

          return self.map
     def get(self,key):
          address=self._gethash(key)
          currentbucket=self.map[address]
          if currentbucket:
               for i in range(len(currentbucket)):
                    if currentbucket[i][0]==key:
                         return currentbucket[i][1]
          else:
               return 'undefined'
     def keys(self):
          keysarray=[]
          for i in range(len(self.map)):
               if self.map[i]:
                    print (self.map[i])
                    keysarray.append(self.map[i][0][0])
          return keysarray          

myhash=Hashmap()
myhash.set('grapes',52)
print(myhash.get('grapes'))
print(myhash.keys())


        


  

                               
