class Solution(object):
    def removeOccurrences(self, s, part):
        
        def maybePopStack(stack):
            if part in stack:
                idx = stack.index(part)
                return stack[:idx]+stack[idx+len(part):]
            return stack
        
        stack = str()
        for i in range(len(s)):
            stack += s[i]
            stack = maybePopStack(stack)
        return stack
