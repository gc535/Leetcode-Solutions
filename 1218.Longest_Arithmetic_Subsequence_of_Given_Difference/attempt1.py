class Solution(object):
    def longestSubsequence(self, arr, difference):
        subseq = {arr[0]:1}
        for n in arr[1:]:
            prev = n - difference
            if prev not in subseq:
                subseq[n] = max(subseq.get(n, 1), 1)
            else:
                l = subseq.pop(prev)
                subseq[n] = l + 1
                
        ret = max([l for k, l in subseq.items()])
        return ret

        
