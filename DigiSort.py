array = [8, 15, 12, 2, 1, 85, 19, 5, 46] #Sorts only positive integers

def digisort(a):
  b = []
  i = 1
  while len(b) < len(a): 
    a = [x-1 for x in a] #Decrement every element by 1
    for x in a:
      if x == 0: #Add i to list b if any 0's are found
        b += [i]
    i += 1
  return b
    
print(digisort(array))
