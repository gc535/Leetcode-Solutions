class Solution(object):
    def carFleet(self, target, position, speed):

        
        sorted_cars = sorted(zip(position, speed))
        num = len(sorted_cars)
        stack = []
        for i in range(num-1, -1, -1):
            s, p = sorted_cars[i][1], sorted_cars[i][0]
            if stack and s > sorted_cars[stack[-1]][1] and ((sorted_cars[stack[-1]][0]-p) / (s-sorted_cars[stack[-1]][1])) <= ((target-sorted_cars[stack[-1]][0]) / sorted_cars[stack[-1]][1]):
                continue
            stack.append(i)
            
                
        return len(stack)
