class Solution(object):
    def canJump(self, nums):
        lastPos = len(nums) -1
        if lastPos <= 0: return True

        min_left = lastPos
        
        for i in range(lastPos-1, -1, -1):
            if nums[i] + i >= min_left:
                min_left = i

        return (min_left == 0)