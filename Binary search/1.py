def bin_search(nums, x):
    low, height = 0, len(nums)
    while low <= height :
        mid = (low + height) // 2
        print(height, low , mid)
        if nums[mid] == x:
            return mid
        elif nums[mid] > x:
            height = mid -1
        else :
            low = mid +1
    return -1
nums = [11, 37, 45, 26, 101, 28, 99 ,53]
# fisrt need to sort
user_x = int(input("Enter x"))