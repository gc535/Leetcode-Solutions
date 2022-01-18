import bisect
#from functools import lru_cache

            
class TimeMap(object):
    def __init__(self):
        self.store = {}  

    def set(self, k, value, timestamp):
        if k not in self.store: self.store[k] = [[], []]
        pos = bisect.bisect_right(a = self.store[k][0], x = timestamp)
        if pos > 0 and self.store[k][0][pos-1] == timestamp:
            self.store[k][1][pos-1] = value
        else:
            self.store[k][0].insert(pos, timestamp)
            self.store[k][1].insert(pos, value)
        
    #@lru_cache(maxsize=(2 * 100000 / 5)) # 2/8 rule
    def get(self, k, timestamp):
        if k not in self.store: return ""
        pos = bisect.bisect_right(a = self.store[k][0], x = timestamp)
        if pos == 0: return ""
        return self.store[k][1][pos-1]


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
