class Solution(object):
    def pushDominoes(self, dominoes):
        """
        :type dominoes: str
        :rtype: str
        """
        split_dominoes = [char for char in dominoes] 
        
        next_lefts =  set()
        next_rights = set()
        for i in range(len(split_dominoes)):
            if split_dominoes[i] == "L":
                next_lefts.add(i)
            elif split_dominoes[i] == "R":
                next_rights.add(i)
        
        while next_lefts or next_rights:
            next_lefts, next_rights, split_dominoes = self.checkStatus(next_lefts, next_rights, split_dominoes)
        
        return "".join(split_dominoes)
    
    def checkStatus(self, left, right, dominoes):
        next_lefts = set()
        next_rights = set()
        
        for pos in left:
            dominoes[pos] = "L"
            next_left = pos - 1
            if next_left >= 0 and dominoes[next_left] == "." and next_left not in right:
                next_lefts.add(next_left)
        
        for pos in right:
            dominoes[pos] = "R"
            next_right = pos + 1
            if next_right < len(dominoes) and dominoes[next_right] == "." and next_right not in left:
                if next_right in next_lefts:
                    next_lefts.remove(next_right)
                else:
                    next_rights.add(next_right)

        return next_lefts, next_rights, dominoes
            