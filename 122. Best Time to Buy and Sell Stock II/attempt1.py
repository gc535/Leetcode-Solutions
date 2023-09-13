class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit, stack = 0, []
        for p in prices:
            if stack and p < stack[-1]: 
                profit += stack[-1] - stack[0]
                stack.clear()
            stack.append(p)
        if stack: profit += stack[-1] - stack[0]
        return profit