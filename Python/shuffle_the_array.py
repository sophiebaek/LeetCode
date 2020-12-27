class Solution(object):
    def shuffle(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: List[int]
        
        >>> Input: nums = [2,5,1,3,4,7], n = 3
        Output: [2,3,5,4,1,7] 
        
        >>> Input: nums = [1,2,3,4,4,3,2,1], n = 4
        Output: [1,4,2,3,3,2,4,1]
        
        >>> Input: nums = [1,1,2,2], n = 2
        Output: [1,2,1,2]
        """
        
        output = []
        
        for i in range(0, n):
            output.append(nums[i])
            output.append(nums[n + i])
        return output
