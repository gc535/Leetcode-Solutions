class Solution(object):
    def new21Game(self, n, k, maxPts):
        if k == 0 or n-k > maxPts: return 1
        perms = [1] + [0] * (n)
        prob = 1.0/maxPts
        prevSum = 1

        for i in range(1, n+1):
            perms[i] = prevSum * prob
            # for next round
            # if cur score >= k, then cur score cannot proceed
            if i < k: prevSum += perms[i]
            # get rid of pre-smallest score prob, which cannot reach i with '+ maxPts'
            if i - maxPts >= 0: prevSum -= perms[i-maxPts]
        
        return sum(perms[k:])