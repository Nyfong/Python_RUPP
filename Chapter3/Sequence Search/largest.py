
# find largest number 
nums = [11, 37, 45, 26, 59, 28, 17,53]

def find_largest(lst):
    largest = lst[0]  # Assume the first element is the largest initially
    for num in lst:
        if num > largest:
            largest = num
    return largest           
            
print("largest: ", find_largest(nums))