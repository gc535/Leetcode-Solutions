class Solution(object):
    def __init__(self):
        self.max_score = []
        self.piles = []
        self.sumToEnd = []
        self.size = 0
        
    def stoneGameII(self, piles):
        """
        :type piles: List[int]
        :rtype: int
        """
        if len(piles) == 1: return piles[0]
        self.piles = piles
        self.size = len(piles)
        self.max_score = [[-1 for i in range(self.size+1)] for j in range(self.size)]
        total = 0
        for i in range(self.size):
            total += piles[self.size-1-i]
            self.sumToEnd.insert(0, total)
            
        self.takeSome(0, 1)
        return self.max_score[0][2]
    
        
    
    def takeSome(self, index, M):
        max_step = 2*M
        lim_step = min(max_step, self.size-index)
        # cached result
        if self.max_score[index][lim_step] != -1:
            return self.sumToEnd[index] - self.max_score[index][lim_step]
        
        if index + max_step >= self.size:
            self.max_score[index][lim_step] = sum(self.piles[index:])
            return 0
        
        max_score = self.max_score[index][lim_step]
        for step in range(1, lim_step+1):
            new_score = sum(self.piles[index:index+step]) + self.takeSome(index+step, max(M, step))
            if new_score > max_score:
                max_score = new_score
        self.max_score[index][lim_step] = max_score
        return self.sumToEnd[index] - max_score
        