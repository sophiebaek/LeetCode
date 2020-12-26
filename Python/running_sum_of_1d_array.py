class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        
        >>> Input: nums = [1,2,3,4]
        Output: [1,3,6,10]
        
        >>> Input: nums = [1,1,1,1,1]
        Output: [1,2,3,4,5]
        
        >>> Input: nums = [3,1,2,10,1]
        Output: [3,4,6,16,17]
        """
        
        if len(nums) == 0:
            return 0
        else:
            output = []
            for i in range(len(nums)):
                new_value = sum(nums[:i+1])
                output.append(new_value)
            return output
