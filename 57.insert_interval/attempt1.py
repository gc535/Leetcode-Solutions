import bisect

class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        l = len(intervals)
        if l == 0: return [newInterval]
        
        left = bisect.bisect_right(intervals, newInterval)
        right = bisect.bisect_left(intervals, [newInterval[1], 0] ) # 0 is a dummy for binary search
        
        kept_left = []
        kept_right = []
        left_bound = newInterval[0]
        right_bound = newInterval[1]

        if left-1 >= 0 and newInterval[0] > intervals[left-1][1]:
            kept_left = intervals[0:left]
        else:
            kept_left = intervals[0:max(0,left-1)]
            if left > 0: left_bound = intervals[max(0,left-1)][0] #just take its left neighbour's left val
        
        if right < l and newInterval[1] < intervals[right][0]:
            kept_right = intervals[right:]
            if right > 0: right_bound = max(intervals[right-1][1], newInterval[1])
            
        else:
            kept_right = intervals[right+1:]
            if right < l: right_bound = intervals[right][1]
            elif right > 0: right_bound = max(intervals[right-1][1], newInterval[1])
            
        return kept_left + [[left_bound, right_bound]] + kept_right