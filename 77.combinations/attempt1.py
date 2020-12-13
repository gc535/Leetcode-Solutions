class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        ret = []
        
        def genNextNum(start, comb):
            if len(comb) == k:
                ret.append(comb)
                
            if k - len(comb) <= n+1 - start:
                for i in range(start, n+1):
                    genNextNum(i+1, comb+[i])
        
        genNextNum(1, [])
        return ret
                    