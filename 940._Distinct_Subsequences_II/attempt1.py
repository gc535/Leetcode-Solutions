class Solution(object):
    def distinctSubseqII(self, s):
        double_cnt_hash = dict()
        ret = 0
        for c in s:
            prev_cnt = ret
            ret += (ret + 1) # new char will create at most n+1 new substr
            ret -= double_cnt_hash.get(c, 0) # deduct double cnt cases if char used before
            double_cnt_hash[c] = double_cnt_hash.get(c, 0) + (ret - prev_cnt) # save num new substr created
        return ret % (10**9 + 7)
