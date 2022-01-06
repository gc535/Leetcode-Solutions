class Solution(object):
    def getCollisionTimes(self, cars):
        """
        :type cars: List[List[int]]
        :rtype: List[float]
        """
        num = len(cars)

        ans = []
        colideStack = []
        for i in range(num-1, -1, -1): 
            time = float('inf')
            if i+1 < num and cars[i][1] > cars[i+1][1]:
                time = (cars[i+1][0] - cars[i][0]) / float((cars[i][1] - cars[i+1][1]))
            
            my_speed, my_pos, colide_id = cars[i][1], cars[i][0], i+1
            while colideStack and time > colideStack[-1][0]: 
                colide_time, colide_id = colideStack.pop()
                colide_car_pos, colide_speed = cars[colide_id][0], cars[colide_id][1]
                if my_speed > colide_speed:
                    time = (colide_car_pos - my_pos) / float(my_speed - colide_speed)
                    
            
            colideStack.append([time, colide_id])
            ans.insert(0, time if time != float('inf') else float(-1))
            
        return ans
