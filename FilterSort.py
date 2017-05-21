array = [8, 15, 12, 2, 1, 85, 19, 5, 46]

def filterSort(a):
  b = max(a)*[None] #Make a list of None that is max(a) long
  for x in a:
    b[x-1] = x #a's value maps to it's index in b: a[0] = 8 --> b[7] = 8
  return list(filter(lambda x: x != None, b)) #Filter out all unused slots

print(filterSort(array))
