def findMinAndMax(L):
  max = L[0]
  min = L[0]
  for value in L:
    if value < min:
      min = value
    
    if value > max:
      max = value
    
  return max,min

result = findMinAndMax([1,2,3,4,5,6,7])
print(result)