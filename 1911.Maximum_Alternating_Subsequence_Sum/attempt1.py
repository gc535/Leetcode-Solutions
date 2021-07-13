class Solution(object):
    def maxAlternatingSum(self, nums):
        maxVal = [0, 0] # max val you can get for the current array if it has odd len or even len
        for n in nums:
            maxVal[0], maxVal[1] = max(maxVal[1]+n, maxVal[0]), max(maxVal[0]-n, maxVal[1])
        return max(maxVal)
