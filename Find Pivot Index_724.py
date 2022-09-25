def pivotIndex(nums):
    
    totalSum = sum(nums)
    right = totalSum
    left = 0
    
    for i in range(len(nums)):
        number = nums[i]
        
        right -= number
        if(left == right):
            return i
        left+= number
    return -1

output = pivotIndex([1,7,3,6,5,6])
print(output)