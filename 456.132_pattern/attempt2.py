class Solution(object):
    def find132pattern(self, nums):
        if (len(nums) < 3): return False
        zones = [[nums[0], None]]
        for num in nums[1:]:
            if zones[-1][1]:
                if zones[-1][0] < num < zones[-1][1]: return True
                if zones[-1][0] > num: zones.append([num, None])
                if zones[-1][1] < num: zones[-1][1] = num
            else:
                if zones[-1][0] < num: zones[-1][1] = num
                else: zones[-1][0] = num
            
            # maybe merge zones
            while len(zones) > 1 and zones[-1][1] :
                if zones[-2][0] < zones[-1][1] < zones[-2][1]: return True
                if zones[-2][1] < zones[-1][1]: zones.pop(-2)
                else: break

        return False
        
            

                