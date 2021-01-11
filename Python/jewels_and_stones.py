class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        """
        :type jewels: str
        :type stones: str
        :rtype: int
        
        >>> Input: jewels = "aA", stones = "aAAbbbb"
        Output: 3
        
        >>> Input: jewels = "z", stones = "ZZ"
        Output: 0
        """
        
        count = 0
        
        for i in range(len(stones)):
            if stones[i] in jewels:
                count += 1
        return count
