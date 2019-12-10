def sort(arr, start, end):
  center = 0
  if(start < end):
    center = (start + end) // 2
    sort(arr, start, center)
    sort(arr, center+1, end)
  else: return
  
  temp = []
  i, j = start, center+1

  # add small item to temp arr 
  while(i<=center and j<=end):
    if(arr[i] <= arr[j]):
      temp.append(arr[i])
      i+=1
    else:
      temp.append(arr[j])
      j+=1
  
  # add remain item
  while(i<=center):
    temp.append(arr[i])
    i+=1
  while(j<=end):
    temp.append(arr[j])
    j+=1
  
  # apply to original
  i=start
  for item in temp:
    arr[i] = item
    i+=1
    # logwrite(len(arr), start, end, f"(apply_to_original)now position: {i}\ntemp_length: {len(temp)}")

def logwrite(length, start, end, content_str):
  print(f"length: {length}, start: {start}, end {end}, \ncontent:\n{content_str}")
