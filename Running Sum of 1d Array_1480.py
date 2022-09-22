class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        
        output = []
        previous_num = 0
        
        for num in nums:
            previous_num = previous_num + num
            output.append(previous_num)
        return output