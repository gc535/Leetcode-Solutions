class Solution(object):
    def increasingTriplet(self, nums):
        if len(nums) < 3: return False

        window = [nums[0], nums[1]]
        minval = min(window)
        invalid_firstTwo = (window[0] >= window[1])
        for i in range(2, len(nums)):
            if nums[i] > window[1] and window[1] > window[0]: return True
            else:
                if (nums[i] > minval) and (invalid_firstTwo or (nums[i] < window[1])):
                    window = [minval, nums[i]]
                elif (nums[i] > window[0]) and (invalid_firstTwo or (nums[i] < window[1])):
                    window[1] = nums[i]
                minval = min(minval, nums[i])

        return False