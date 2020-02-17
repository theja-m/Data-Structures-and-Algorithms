def add80(n):
  print('Long time')
  return n+80

print(add80(5))
print(add80(5))

#Memoization 1

cache = {}

def memoizedadd80(n):
  if n in cache:
    return n + 80
  else:
    print('Long time')
    cache[n] = n+80
    return cache[n]

print(memoizedadd80(6))
print(memoizedadd80(6))

#Memoization 2
# https://docs.python.org/3.3/library/functools.html --> Doc for lru_cache

from functools import lru_cache

@lru_cache(maxsize = 1000)
def memoized2add80(n):
  return n + 80


print(memoized2add80(8))
print(memoized2add80(8))
print(memoized2add80.cache_info())



