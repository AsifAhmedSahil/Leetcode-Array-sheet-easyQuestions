def removeDuplicate(nums):
    i=0
    while(i<len(nums)):
        j = i+1
        while(j<len(nums) and nums[i] == nums[j]):
            nums.pop(j)
        i=j
    return nums

# output = removeDuplicate([1,1,2])
output = removeDuplicate([1,1,2,2,3])
print(output)
            