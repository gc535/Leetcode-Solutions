import heapq

class Solution(object):
    def eatenApples(self, apples, days):
        lastday = len(apples)
        day = 0
        apple_heap = []
        heapq.heapify(apple_heap)
        ret = 0

        while day < lastday:
            if apples[day] > 0:
                heapq.heappush(apple_heap, [day+days[day], apples[day]])
            
            if apple_heap and apple_heap[0][0] > day:
                ret += 1
                apple_heap[0][1] -= 1
                if apple_heap[0][1] == 0:
                    heapq.heappop(apple_heap)
            day += 1

            while apple_heap and apple_heap[0][0] <= day:
                heapq.heappop(apple_heap)

        
        while apple_heap:
            [expire, counts] = heapq.heappop(apple_heap)
            if day < expire:
                jump_to = min(expire, day + counts)
                ret += jump_to - day
                day = jump_to

        return ret