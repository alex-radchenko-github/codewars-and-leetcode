def trap(height):

  if height == []:
      return 0

  rez = []
  max_l = max(height)
  max_l_i = height.index(max_l)
  left = height[:max_l_i+1]
  right = height[max_l_i:][::-1]
  max_n = 0
  for i in left:
      if i > max_n:
          max_n = i
      else:
          rez.append(max_n - i)
  max_n = 0
  for i in right:
      if i > max_n:
          max_n = i
      else:
          rez.append(max_n - i)
  return sum(rez)

print(trap([0,1,0,2,1,0,1,3,2,1,2,1]))