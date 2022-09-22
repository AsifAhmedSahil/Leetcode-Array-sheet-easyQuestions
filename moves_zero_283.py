# move the zero with out space complexity
#  in one place or one array****


def moves_zero(nums):
    
    i = 0
    j = 0
    
    while(j < len(nums)):
        if(nums[j] != 0):
            nums[i] , nums[j] = nums[j] , nums[i]
            i = i+1
        j = j+1
    return nums
    
output = moves_zero([0,1,3,0,12]);
print(output)
    