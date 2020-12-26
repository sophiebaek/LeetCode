class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        
        >>> Input: nums = [2,2,1]
        Output: 1
        
        >>> Input: nums = [4,1,2,1,2]
        Output: 4
        
        >>> Input: nums = [1]
        Output: 1
        """
        
        # Initialization
        num_array = []
        
        # Create num_array (no repetition)
        for i in range(len(nums)):
            if nums[i] not in num_array:
                num_array.append(nums[i])
            else:
                num_array.remove(nums[i])
        return num_array[0]
