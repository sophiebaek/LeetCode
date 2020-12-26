class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        if len(nums) == 0:
            return 0
        else:
            output = []
            for i in range(len(nums)):
                new_value = sum(nums[:i+1])
                output.append(new_value)
            return output
