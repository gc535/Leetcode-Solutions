class Solution(object):
    def isReachableAtTime(self, sx, sy, fx, fy, t):
        distx, disty = abs(fx - sx), abs(fy - sy)
        if (distx + disty) == 0 and t == 1: return False
        mintime = max(distx, disty)
        return t >= mintime
        
