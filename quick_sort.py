def sort(arr, start, end):
  if(start < end):
    pivot = calc_pivot(arr, start, end, end)
    sort(arr, start, pivot-1)
    sort(arr, pivot+1, end)

def calc_pivot(arr, start, end, pivot_position):
  x = arr[pivot_position]
  i = start-1
  for j in range(start, end+1):
    if(arr[j] < x and j != pivot_position):
      if(i+1 == pivot_position): i+=1
      i+=1
      arr[i], arr[j] = arr[j], arr[i]
  arr[i+1], arr[pivot_position] = arr[pivot_position], arr[i+1]

  return i+1
