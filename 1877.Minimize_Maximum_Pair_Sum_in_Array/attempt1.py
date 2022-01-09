class Solution(object):
    def minPairSum(self, nums):
        ret = 0
        nums = sorted(nums)
        while nums:
            ret = max(nums.pop(0) + nums.pop(), ret)
        return ret
