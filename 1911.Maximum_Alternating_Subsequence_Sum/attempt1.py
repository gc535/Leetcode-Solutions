class Solution(object):
    def maxAlternatingSum(self, nums):
        maxVal = [[0, 0]] # max val you can get for the current array if it has odd len or even len
        for n in nums:
            maxVal.append([max(maxVal[-1][1]+n, maxVal[-1][0]), max(maxVal[-1][0]-n, maxVal[-1][1])])
        return max(maxVal[-1])
