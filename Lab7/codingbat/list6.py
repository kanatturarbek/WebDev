def has22(nums):
  has=False
  for i in range(len(nums)-1):
    if nums[i]==2:
      if nums[i+1]==2:
        has=True
  return has
