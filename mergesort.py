def mergesort(array):
  if len(array) <= 1:
    return array

  half = len(array) // 2

  leftHalf = array[:half]
  rightHalf = array[half:]

  leftHalf = mergesort(leftHalf)
  rightHalf = mergesort(rightHalf)
    
  resultArray = []
  i = 0
  j = 0

  for k in range(len(array)):
    if i < len(leftHalf) and j < len(rightHalf):
      if leftHalf[i] < rightHalf[j]:
        resultArray.append(leftHalf[i])
        i += 1
      else:
        resultArray.append(rightHalf[j])
        j += 1
  
  resultArray += leftHalf[i:]
  resultArray += rightHalf[j:]
  return resultArray


print('Hello, this is an exemple of the MergeSort algorithm. Please, enter any amount of numbers separated by commas: ')

array = [int(num) for num in input().split(',')]

print(mergesort(array))