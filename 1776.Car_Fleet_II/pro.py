    def getCollisionTimes(self, A):
        stack = []
        n = len(A)
        res = [-1] * n
        for i in range(n-1, -1, -1):
            p, s = A[i]
            while stack and (s <= A[stack[-1]][1] or (A[stack[-1]][0] - p) / (s - A[stack[-1]][1]) >= res[stack[-1]] > 0):
                stack.pop()
            if stack:
                res[i] = (A[stack[-1]][0] - p) / (s - A[stack[-1]][1])
            stack.append(i)
        return res
