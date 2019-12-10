def sort(arr, start, end):
  k = max(arr)
  c, b = [], []

  for i in range(k+1):
    c.append(0)
  for i in range(start,end+1):
    b.append(0)  
  for i in range(start,end+1):
    c[arr[i]] += 1
  for i in range(k):
    c[i+1] += c[i]
  for i in range(end, -1, -1):
    b[c[arr[i]]-1] = arr[i]
    c[arr[i]] -= 1

  print(c)

  # copy
  for i in range(start,end+1):
    arr[i] = b[i]
