class Solution(object):
    def new21Game(self, n, k, maxPts):
        perms = [0] * (n+1)
        perms[0] = 1
        prob = 1.0/maxPts

        def perm(x):
            if perms[x] != 0: return perms[x]
            cases = [x-n for n in range(1, maxPts+1) if (x-n >= 0) and (x-n < k)]
            perms[x] = sum(perm(c)*prob for c in cases)
            return perms[x]
        
        return sum(perm(x) for x in range(k, n+1))