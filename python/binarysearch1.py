#count negative numbers in a sorted matrix
def countNegative(grid,target):
  count = 0
  for row in grid:
      for num in row:
          if num<target:
             count +=1
  return count





grid = [[4, 3, 2, 1], [3, 2, 1, -1], [1, 1, -1, -2], [-1, -1, -2, -3]] 
target = 0
result = countNegative(grid,target)
print(result)