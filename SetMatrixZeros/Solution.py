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
