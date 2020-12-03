class Solution(object):
    def __init__(self):
        self.table = {}
        
        
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        if len(s) < 10: return []
        
        self.genTable("", 0)      
        ret = set()
        for i in range(10, len(s)+1):
            if self.table[s[i-10:i]] > 0:
                ret.add(s[i-10:i])
            else:
                self.table[s[i-10:i]] += 1
        return list(ret)    
    
    def genTable(self, s, l):
        for char in ["A", "T", "G", "C"]:
            if len(s) == 9:
                self.table[s+char] = 0
            else:
                self.genTable(s+char, l+1)
        
            