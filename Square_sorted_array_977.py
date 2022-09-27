'''
Approach --> 1st e 2 ta pointer set kore dibo --> left & right --> then left ,right er value k square krbo
        korar por check krbo kontya boro jeta boro oita k empty array te append kore dibo --> then finally array ta k return korbo inverse kore mane choto to boro form e 

'''

def squareSorted(nums):
    
    res = []
    l,r = 0 , len(nums)-1

    while l <= r:
        if nums[l] * nums[l] > nums[r] * nums[r]:
            res.append(nums[l] * nums[l])
            l = l+1
        else:
            res.append(nums[r] * nums[r])
            r = r-1
    return res[::-1]

print(squareSorted([-4,-3,0,5,10]))