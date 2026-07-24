class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        leng=len(matrix)
        row=len(matrix[0])
        rel=[]
        for i in range(row):
            row1=[]
            for j in range(leng):
                row1.append(matrix[j][i]) 
            rel.append(row1)
        return rel
