class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        matLen = len(matrix)
        for i in range(0, matLen):
            for j in range(0, len(matrix[i])):
                if matrix[i][j] == 0:
                    matrix[i][j] = None
        
        for i in range(0, matLen):
            for j in range(0, len(matrix[i])):
                if matrix[i][j] == None:
                    for k in range(0, matLen):
                        if matrix[k][j] != None:
                            matrix[k][j]=0
                    for k in range(0, len(matrix[i])):
                        if matrix[i][k] != None:
                            matrix[i][k] = 0
        for i in range(0, matLen):
            for j in range(0, len(matrix[i])):
                if matrix[i][j] == None:
                    matrix[i][j] = 0
                    
    '''
    Runtime: 120 ms, faster than 96.69% of Python3 online submissions for Set Matrix Zeroes.
    Memory Usage: 15.2 MB, less than 46.75% of Python3 online submissions for Set Matrix Zeroes.
    '''
    def setZeroesOptimized(self, matrix: List[List[int]]) -> None:
        count = 0
        matLen = len(matrix)
        rowLen = len(matrix[0])
        for i in range(0, matLen):
            for j in range(0, rowLen):
                if matrix[i][j] == 0:
                    matrix[i][0] = None
                    matrix[0][j] = None
                    if j==0:
                        count|=1
                    if i==0:
                        count|=2

        for i in range(matLen-1, 0, -1):
            for j in range(rowLen-1, 0, -1):
                if (matrix[i][0] == None or matrix[0][j] == None):
                    matrix[i][j] = 0
        for i in range(matLen-1, -1, -1):
            if count&1==1 or matrix[i][0]==None:
                matrix[i][0] =0
        
        for i in range(rowLen-1, -1, -1):
            if count&2==2 or matrix[0][i]==None:
                matrix[0][i] =0
