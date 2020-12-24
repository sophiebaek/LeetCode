class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
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
