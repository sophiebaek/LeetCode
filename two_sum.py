class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        sum_value = 0
        
        for i in range(len(nums)):
            if sum_value != target:
                sum_value = nums[i]
                for j in range(i+1, len(nums)):
                    if sum_value != target:
                        sum_value = nums[i]
                        sum_value += nums[j]
                        if sum_value == target:
                            result = [i, j]
                            return result
                    else:
                        if sum_value == target:
                            if nums[i] + nums[j] == target:
                                result = [i, j]
                                return result 
                        else:
                            result = [i, j-1]
                            return result
            else:
                for j in range(i+1, len(nums)):
                    if nums[i] + nums[j] == 0:
                        result = [i, j]
                        return result
