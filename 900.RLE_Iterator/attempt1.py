class RLEIterator(object):
    def __init__(self, encoding):
        self.encoding = [[encoding[i*2], encoding[i*2+1]] for i in range(len(encoding)/2)]
        print self.encoding

    def next(self, n):        
        ret = -1
        while self.encoding and n:
            avail, val, cnt = self.encoding[0][0], self.encoding[0][1], 0
            if avail > n:
                self.encoding[0][0] = avail - n
                cnt = n
            else:
                self.encoding.pop(0)
                cnt = avail
            ret = val
            n -= cnt
        return ret if n == 0 else -1
