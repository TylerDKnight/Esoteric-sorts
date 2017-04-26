array = [8, 15, 12, 2, 1, 85, 19, 5, 46]

def filterSort(a):
  b = max(a)*[None]
  for x in a:
    b[x-1] = x
  return list(filter(lambda x: x != None, b))

print(filterSort(array))
