array = [8, 15, 12, 2, 1, 85, 19, 5, 46]

def cheatSort(a):
  if len(a) == 0:
    return []
  least_i = a.index(min(a)) #Find the smallest number, O(n)
  return [a[least_i]] + cheatSort(a[:least_i]+a[(least_i+1):]) #Tack it at the front, trim list and repeat

print(cheatSort(array))
