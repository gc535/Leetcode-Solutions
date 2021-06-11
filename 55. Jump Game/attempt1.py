class Solution(object):
    def canJump(self, nums):
        lastPos = len(nums) -1
        if lastPos <= 0: return True

        markers = [False for i in range(lastPos)]
        markers.append(True)
        
        for i in range(lastPos-1, -1, -1):
            dist = lastPos - i
            if nums[i] >= dist:
                markers[i] = True
            else:
                markers[i] = any([markers[i + step] for step in range(nums[i]+1)])
        return markers[0]