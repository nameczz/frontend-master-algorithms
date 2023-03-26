import math

def binary_search(arr,target):
  min = 0
  max = len(arr)
  while(min < max) :
    mid = math.floor((min+max)/2)
    midVal = arr[mid]
    if midVal == target:
      return True
    if midVal < target:
      min = mid + 1
    else:
      max = mid
  return False
    
    

