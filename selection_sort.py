def sort(arr, start, end):
  for i in range(end, start, -1):
    max_index = arr.index(max(arr[:i+1]))
    arr[i], arr[max_index] = arr[max_index], arr[i]
