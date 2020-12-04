class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        seen = {}
        for num in nums:
            if num in seen:
                seen[num] -= 1
                if seen[num] == 0: del seen[num]
            else:
                seen[num] = 2
        
        for k, v in seen.items():
            return k