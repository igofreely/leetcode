class Solution:
    class Node(object):
        def __init__(self, i, j, result):
            self.i = i
            self.j = j
            self.result = result

    def solveNQueens(self, n: int):
        if n==1:
            return [["Q"]]
        result=self.solve(n)
        ret=["".join(["."for i in range(n)])for i in range(n)]
        retret=[]
        for r in result:
            ret2=copy.deepcopy(ret)
            for rr in r:
                ret2[rr[0]]=ret2[rr[0]][:rr[1]]+"Q"+ret2[rr[0]][rr[1]+1:]
            retret.append(ret2)
        return retret

    def solve(self, n):
        # visit = [[False for i in range(n)] for i in range(n)]
        sovles=[]
        dq = collections.deque()
        for firstj in range(n):
            dq.append(self.Node(0, firstj, [[0, firstj]]))
            while len(dq) > 0:
                n1 = dq[0]
                dq.popleft()
                for jj in range(n):
                    if jj != n1.j:
                        for ii in n1.result:
                            if jj == ii[1] or abs(n1.i + 1 - ii[0]) == abs(jj - ii[1]) or n1.i + 1 + jj == ii[0] + ii[1]:
                                break
                        else:
                            np = copy.deepcopy(n1.result)
                            np.append([n1.i + 1, jj])
                            dq.append(self.Node(n1.i + 1, jj, np))
                            if len(np)==n:
                                sovles.append(np)
        return sovles
