import bisect

class SnapshotArray(object):

    def __init__(self, length):
        self.array_snp = [[[0, 0]] for i in range(length)]
        self.snp_idx = 0
        
    def set(self, index, val):
        if self.array_snp[index][-1][0] == self.snp_idx:
            self.array_snp[index][-1][1] = val
        else:
            self.array_snp[index].append([self.snp_idx, val])

    def snap(self):
        self.snp_idx += 1
        return self.snp_idx - 1

    def get(self, index, snap_id):
        pos = bisect.bisect(self.array_snp[index], [snap_id + 1])
        return self.array_snp[index][pos-1][1]
