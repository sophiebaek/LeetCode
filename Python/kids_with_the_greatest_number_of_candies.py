class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        
        >>> Input: candies = [2,3,5,1,3], extraCandies = 3
        Output: [true,true,true,false,true]
        
        >>> Input: candies = [4,2,1,1,2], extraCandies = 1
        Output: [true,false,false,false,false] 
        
        >>> Input: candies = [12,1,12], extraCandies = 10
        Output: [true,false,true]
        """
        
        output = []
        
        for i in range(len(candies)):
            get_extra = candies[i] + extraCandies
            if get_extra >= max(candies):
                output.append(True)
            else:
                output.append(False)
        return output
