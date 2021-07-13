class Solution(object):
    def sumGame(self, num):
        halfLine = len(num)/2
        left_sum = right_sum = left_q = right_q = 0
        for i in range(halfLine):
            if num[i] == "?":
                left_q += 1
            else:
                left_sum += int(num[i])
            
            if num[i+halfLine] == "?":
                right_q += 1
            else:
                right_sum += int(num[i+halfLine])
        
        dist = left_sum - right_sum
        addon = right_q - left_q

        if dist == 0: return True if addon % 2 != 0 else False
        if (dist > 0 and addon <= 0) or (dist < 0 and addon >=0): return True
        
        if dist < 0:
            dist, addon = -dist, -addon
        if 9 * (addon/2 + addon%2) > dist or \
            9 * (addon/2) < dist: return True
        else: return False
 

        
        
        