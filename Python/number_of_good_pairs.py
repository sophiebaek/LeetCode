class Solution(object):
    def numIdenticalPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        
        >>> Input: nums = [1,2,3,1,1,3]
        Output: 4
        
        >>> Input: nums = [1,1,1,1]
        Output: 6
        
        >>> Input: nums = [1,2,3]
        Output: 0
        """
        
        num_good_pairs = 0
        
        for i in range(0, len(nums)):
            for j in range(1, len(nums)):
                if nums[0] == nums[j]:
                    num_good_pairs += 1
            nums.remove(nums[0])
        return num_good_pairs
