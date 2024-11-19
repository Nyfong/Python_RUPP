def find_two (nums):
    x = y =0
    for i in range(1, len(nums)):
        if nums[x] < nums [i]:
            x=i
            print("a",end="")
        elif nums[y] > nums[i]:
              y = i
              print("a", end="")
        print(i,end="")    
    return x, y
nums = [11, 37, 45, 26, 59, 28, 17, 53]
i, j = find_two(nums)
print(nums [i], nums [j])