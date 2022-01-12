class Trie:
    def __init__(self):
        self.child = [None for i in range(26)]
        self.index = set()
    
    def addStr(self, string, i):
        self.index.add(i)
        if len(string) == 0: return
        char = ord(string[0]) - 97 
        
        if self.child[char] is None:
            self.child[char] = Trie()
        self.child[char].addStr(string[1:], i)
    
    def findStr(self, string):
        if len(string) == 0: return self.index
        char = ord(string[0]) - 97
        if self.child[char] is None: return set()
        return self.child[char].findStr(string[1:])
    

class WordFilter(object):
    def __init__(self, words):
        self.prefix_trie = Trie()
        self.surfix_trie = Trie()
        
        for i in range(len(words)):
            self.prefix_trie.addStr(words[i], i)
            self.surfix_trie.addStr(words[i][::-1], i)

    def f(self, prefix, suffix):
        set1, set2 = self.prefix_trie.findStr(prefix), self.surfix_trie.findStr(suffix[::-1])
        ret = -1
        for i in set1:
            if i in set2: ret = max(i, ret)
        return ret
