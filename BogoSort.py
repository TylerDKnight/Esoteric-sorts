import random
import sys

array = [8, 15, 12, 2, 1, 85, 19, 5, 46]

def bogo(a):
  random.seed()
  while not(isSorted(a)): #While not sorted
    for i in range(len(a)-1): #Randomly shuffle
      r = random.randrange(i, len(a))
      temp = a[i]
      a[i] = a[r]
      a[r] = temp
  return a
  
def isSorted(a): #Verify is sorted
  last = -sys.maxsize - 1
  for x in a:
    if last > x:
      return False
    last = x
  return True
  
  
print(bogo(array))
    
    
