from random import randint

class hash_lis:

    def __init__(self,size):
        self.size = size
        self.mydict = ['None']*self.size
        self.add_list = []

    def __str__(self):
        return str(self.__dict__)

    def _hash(self):
        while True:
            x = randint(0,self.size-1)
            if x not in self.add_list:
                return x

    def _set(self,key,value):
        add = self._hash()
        self.mydict[add] = [key,value]
        self.add_list.append(add)

    def _get(self,key):
        for i in self.add_list:
            if self.mydict[i][0] == key:
                return self.mydict[i][1]

    def _key(self):
        key_arr = []
        for i in self.add_list:
            key_arr.append(self.mydict[i][0])
        return key_arr 


h = hash_lis(3)
h._set('grapes',1000)
h._set('lemon',20)
h._set('grap',100)

x=h._get('grapes')
print(x)
x=h._get('lemon')
print(x)
x=h._get('grap')
print(x)
key_arr = h._key()
print(h)
print(key_arr)
