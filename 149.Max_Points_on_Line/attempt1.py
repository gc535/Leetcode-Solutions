import sys

class Solution(object):
    def maxPoints(self, points):
        nums = len(points)
        if nums < 2: return nums
        
        # get greatest common divisor
        def computeGCD(x, y):
            while(y):
                x, y = y, x % y
            return x

        # get slope
        def getSlope(deltaX, deltaY):
            if deltaX == 0: 
                slope = (sys.maxint, sys.maxint)
            elif deltaY == 0:
                slope = (0, 0)
            else:
                if deltaX < 0:
                    deltaX, deltaY = -deltaX, -deltaY
                gcd = computeGCD(deltaY, deltaX)
                slope = (deltaY/gcd, deltaX/gcd)
            return slope
    
        ret = 0
        for i in range(nums):
            slopDict = {}
            for j in range(i+1, nums):                
                deltaX = points[j][0] - points[i][0]
                deltaY = points[j][1] - points[i][1]
                slope = getSlope(deltaX, deltaY)
                
                if slope in slopDict:
                    slopDict[slope] += 1
                else:
                    slopDict[slope] = 2
                ret = max(ret, slopDict[slope])
        
        return ret     