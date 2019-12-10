def sort(arr, start, end):
  for i in range(start+1, end+1):
    x = arr[i]
    for j in range(i-1,-1,-1):
      if(x >= arr[j]):
        j+=1
        break
      else:
        arr[j+1] = arr[j]
    arr[j] = x
    print(arr)
