def first_recurring_character(array):

  total_items = len(array)-1
  first_RC = None
  for i in range(total_items):
      for j in range(i+1, total_items):
          if array[i] == array[j]:
              if first_RC is None or first_RC > j:
                  first_RC = j
  if first_RC:
      return array[first_RC]
  return None

def first_recurring_character_hashtable(array):
  my_dict = {}
  for i in range(0,len(array)):
    if array[i] in my_dict:
      return array[i]
    else:
      my_dict[array[i]]=i
  return None
  

my_list = [2,1,1,2,3,4,5] # Output 1 instead of 2
first_RC = first_recurring_character(my_list)
first_RC_hashtable = first_recurring_character_hashtable(my_list)
print(first_RC)
print(first_RC_hashtable)
