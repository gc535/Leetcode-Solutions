import bisect
import sys

class SnapshotArray(object):

    def __init__(self, length):
        self.array_snp = [[] for i in range(length)]
        self.array = [0 for i in range(length)]
        self.updated = [True for i in range(length)]
        self.snp_idx = -1
        
    def set(self, index, val):
        self.updated[index] = (len(self.array_snp[index]) == 0) or (self.array_snp[index][-1][1] != val) # not same as last snp
        self.array[index] = val

    def snap(self):
        self.snp_idx += 1
        for i in range(len(self.array)):
            if self.updated[i]:
                self.array_snp[i].append([self.snp_idx, self.array[i]])
                self.updated[i] = False
        return self.snp_idx
        

    def get(self, index, snap_id):
        pos = bisect.bisect_right(self.array_snp[index], [snap_id, sys.maxint])
        return self.array_snp[index][pos-1][1]
        
