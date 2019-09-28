

def max_list_iter(int_list):  # must use iteration not recursion
   """finds the max of a list of numbers and returns the value (not the index)
   If int_list is empty, returns None. If list is None, raises ValueError"""
   #TODO: more testcases

   if int_list == None:
      raise ValueError("ValueError")
   if not int_list:
      return None
   '''
   for j in int_list:
      result = isinstance(j, int)
      if result == False:
         raise TypeError("TypeError")
   '''
   maxInt = int_list[0]
   for i in int_list:
      if i > maxInt:
         maxInt = i
   return maxInt


def reverse_rec(int_list):   # must use recursion
   """recursively reverses a list of numbers and returns the reversed list
   If list is None, raises ValueError"""
   if int_list == None:
      raise ValueError("ValueError")
   if len(int_list) == 0:
      return []

   return [int_list.pop()] + reverse_rec(int_list)




def bin_search(target, low, high, int_list):  # must use recursion
   """searches for target in int_list[low..high] and returns index if found
   If target is not found returns None. If list is None, raises ValueError """
   '''if int_list == None:
      raise ValueError

   if (target < int_list[low] or target > int_list[high]):
      return None
   if (len(int_list) == 1):
      if target == int_list[0]:
         return 0
      else:
         return None
   if high >= low:

      mid = low + (high - 1) // 2
      if (target == int_list[mid]):
         return mid
      elif (target < int_list[mid]):
         return bin_search(target, low, mid - 1, int_list)
      else:
         return bin_search(target, mid + 1, high,int_list)
   else:
      return None'''
   if int_list == None:
      raise ValueError

   if int_list == []:
      return None
   if (target < int_list[low] or target > int_list[high]):
      return None

   if high >= low:

      mid = low + (high - low) // 2

      # If element is present at the middle itself
      if int_list[mid] == target:
         return mid

         # If element is smaller than mid, then it can only
      # be present in left subarray
      elif int_list[mid] > target:
         return bin_search(target, low, mid - 1, int_list)

         # Else the element can only be present in right subarray
      else:
         return bin_search(target, mid + 1, high, int_list)

'''
   else:
      # Element is not present in the array
      return None
'''


