# https://leetcode.com/problems/n-queens/

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        
        def colocateQueen(n, i):
            for j in range(n):
                if j not in col and j + i not in diag1 and j - i not in diag2: 
                    if n - 1 == i:
                        chess[n - 1][j] = "Q"
                        arr = ["".join(row) for row in chess]
                        ans.append(arr)
                        chess[n - 1][j] = "."
                    else:
                        col.add(j)
                        diag1.add(j + i)
                        diag2.add(j - i)
                        chess[i][j] = "Q"
                        colocateQueen(n, i + 1)
                        chess[i][j] = "."                    
                        col.discard(j)
                        diag1.discard(j + i)
                        diag2.discard(j - i)        
        ans = []
        chess = [["." for j in range(n)] for i in range(n)]
        col, diag1, diag2 = set(), set(), set()        
        colocateQueen(n, 0)
        
        return ans