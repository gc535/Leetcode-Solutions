class Solution(object):
    def findLengthOfShortestSubarray(self, arr):
        l = len(arr)
        if l <= 1: return 0
        
        def findLeft(arr):
            for i in range(1, len(arr)):
                if arr[i] < arr[i-1]:
                    return i-1
            return -1 

        def findRight(arr):
            l = len(arr)
            for i in range(l-2, -1, -1):
                if arr[i] > arr[i + 1]:
                    return i + 1
            return -1

        left = findLeft(arr)
        if left == -1 : return 0
        else:
            right = findRight(arr)
            i = 0
            maxlen = max(left + 1, l - right)
            while i <= left and right < l:
                if arr[i] <= arr[right]:
                    maxlen = max(maxlen, i + 1 + l - right)
                    i += 1
                else:
                    right += 1

            maxlen = max(maxlen, i + l - right)
            return l - maxlen