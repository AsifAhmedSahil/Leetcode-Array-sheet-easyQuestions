def majorityElement(nums):
    
    dict = {}
    for num in nums:
        if  num not in dict:
            dict[num] = 1
        if dict[num] > len(nums)//2:
            return num 
        else:
            dict[num] += 1
            
output = majorityElement([3,2,3])
print(output)