"""
Consider the following operations:
0 ^ x = x,

x ^ x = 0；

x & ~x = 0,

x & ~0 =x;

if x appears once, a=x, b=0;
if x appears twice, a=0,b=x;
if x appears triple, a=0,b=0;
Therefore, the first case correponds to the single number, a will be the answer.
"""


class Solution(object):
    def singleNumber(self, nums):
        a,b=0,0
        for num in nums:
            a=(a^num)&(~b)
            b=(b^num)&(~a)
            
        return a