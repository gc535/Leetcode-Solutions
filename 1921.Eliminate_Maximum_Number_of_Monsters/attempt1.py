import heapq

class Solution(object):
    def eliminateMaximum(self, dist, speed):
        minReachCity = [dist[i]/speed[i] + (1 if (dist[i]%speed[i] > 0) else 0) for i in range(len(speed))]
        heapq.heapify(minReachCity)

        mins = 0
        result = 0
        while minReachCity:
            toKill = heapq.heappop(minReachCity)
            if toKill <= mins: return result
            result += 1
            mins += 1
            
        return result