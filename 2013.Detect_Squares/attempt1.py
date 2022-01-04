class DetectSquares(object):

    def __init__(self):
        self.samex = dict()
        self.samey = dict()
        self.points = dict()

    def add(self, point):
        """
        :type point: List[int]
        :rtype: None
        """
        [x, y] = point
        if x not in self.samex: self.samex[x] = list()
        self.samex[x].append([x, y])
        
        if y not in self.samey: self.samey[y] = list()
        self.samey[y].append([x, y])
        
        self.points[(x, y)] = self.points.get((x, y), 0) + 1

    def count(self, point):
        [x, y] = point
        targety_dp = {}
        targetxy_dp = {}
        cnt = 0
        for [samex, targety] in self.samex.get(x, []):
            if targety in targety_dp:
                cnt += targety_dp[targety]
                continue
                
            if targety == y: 
                targety_dp[y] = 0
                continue
                
            y_res = 0
            for [targetx, targety] in self.samey.get(targety, []):
                if (targetx, targety) in targetxy_dp:
                    y_res += targetxy_dp[(targetx, targety)]
                    continue
                    
                x_dist, y_dist = targetx - x, targety - y
                xy_res = 0
                if x_dist == y_dist or x_dist == -y_dist:
                    diag = (x + x_dist, y)
                    xy_res = self.points.get(diag, 0)
                    
                targetxy_dp[(targetx, targety)] = xy_res
                y_res += xy_res
                
            targety_dp[targety] = y_res
            cnt += y_res
        
        return cnt

             


# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)
