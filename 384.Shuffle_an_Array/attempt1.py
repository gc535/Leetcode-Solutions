import copy
import random

class Solution(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.ori = nums
        self.operand = copy.deepcopy(nums)
        

    def reset(self):
        """
        Resets the array to its original configuration and return it.
        :rtype: List[int]
        """
        return self.ori
        

    def shuffle(self):
        """
        Returns a random shuffling of the array.
        :rtype: List[int]
        """
        for i in range(len(self.ori)-1, -1, -1):
            pos = random.randint(0, i)
            self.operand[i], self.operand[pos] = self.operand[pos], self.operand[i]
        return self.operand


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()
