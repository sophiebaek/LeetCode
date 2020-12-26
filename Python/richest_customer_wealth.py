class Solution(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        
        >>> Input: accounts = [[1,2,3],[3,2,1]]
        Output: 6
        
        >>> Input: accounts = [[1,5],[7,3],[3,5]]
        Output: 10
        
        >>> Input: accounts = [[2,8,7],[7,1,3],[1,9,5]]
        Output: 17
        """
        
        max_wealth = 0
        
        for customer in range(len(accounts)):
            wealth = sum(accounts[customer])
            if wealth > max_wealth:
                max_wealth = wealth
        return max_wealth
