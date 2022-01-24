class Solution(object):
    def asteroidCollision(self, asteroids):
        ret = []
        for a in asteroids:
            if a < 0:
                while ret and ret[-1] > 0 and ret[-1] + a < 0: ret.pop()
                if ret and ret[-1] + a >= 0:
                    if ret[-1] + a == 0: ret.pop()
                    continue
            ret.append(a)
        return ret
