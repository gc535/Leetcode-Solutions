class Solution(object):
      
    #########################
    ### Time limit exceed ###
    #########################

    # O(n^2) always TLE, can be O(n)

    def find132pattern(self, nums):
        zones = []
        for num in nums:
            inserted = False
            for zone in zones:
                if num > zone[0]:
                    if zone[1] and num < zone[1]: return True
                    zone[1] = num
                    inserted = True
            if not inserted: zones.append([num, None])
            

        
            