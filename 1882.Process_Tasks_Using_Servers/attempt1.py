import heapq
class Solution(object):
    def assignTasks(self, servers, tasks):
        numTasks = len(tasks)
        if len(servers) == 1: return [0 for i in range(numTasks)]
        
        aval = []
        busy = []
        heapq.heapify(aval)
        heapq.heapify(busy)
        for i in range(len(servers)):
            heapq.heappush(aval, [servers[i], i])

        ret = []
        time = 0
        for i in range(numTasks):
            time = max(time, i)
            if len(aval) == 0:
                time = busy[0][0]

            # check if busy server becomes available again
            while len(busy) > 0 and busy[0][0] <= time:
                [_, index] = heapq.heappop(busy)
                heapq.heappush(aval, [servers[index], index])

            # assign tasks to first available server in the min heap
            taskTime = tasks[i]
            [_, index] = heapq.heappop(aval)
            heapq.heappush(busy, [time + taskTime, index])
            ret.append(index)

        return ret