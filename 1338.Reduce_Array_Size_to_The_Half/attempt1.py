import heapq

class Solution(object):
    def minSetSize(self, arr):
        occurance = {}
        for e in arr:
            if e not in occurance:
                occurance[e] = 1
            else:
                occurance[e] += 1
        
        pq = list()
        heapq.heapify(pq)
        for num, occur in occurance.items():
            heapq.heappush(pq, [-occur, num])
        
        size = 0
        cut_size = 0
        cnt = len(arr)
        while pq and (cut_size * 2 < cnt):
            cut_size -= heapq.heappop(pq)[0]
            size += 1

        return size