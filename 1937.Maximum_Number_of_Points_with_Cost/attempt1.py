class Solution(object):
    def maxPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        dp = [0 for i in range(len(points[0]))] # each dp[c] means the max val points[r][c] can get from previous row
        for r in range(len(points)):
            dp[0] += points[r][0] 
            for c in range(1, len(points[0])): # forward pass
                dp[c] = max(dp[c]+points[r][c], dp[c-1]-1)
            
            for c in range(len(points[0])-2, -1, -1): # backward pass
                dp[c] = max(dp[c], dp[c+1]-1)
        
        return max(dp)
