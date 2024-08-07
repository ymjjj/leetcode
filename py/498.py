from typing import List
class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        m=len(mat)
        n=len(mat[0])
        i=0
        j=0
        p=0
        array = [0 for _ in range(m*n)]
        self.diagonaltraversal(array,mat,i,j,p,0)
        return array
    def diagonaltraversal(self,array:List[int],mat: List[List[int]],i:int,j:int,p:int,d:int) -> List[int]:
        if len(mat)==1:
            for k in range(len(mat[0])):
                array[k]=mat[0][k]
            return array
        if len(mat[0])==1:
            for k in range(len(mat)):
                array[k]=mat[k][0]
            return array
        
        if p==len(mat)*len(mat[0])-1:
            array[p]=mat[i][j]
            return array
        
        if i==0 and j==0:
            array[0]=mat[i][j]
            if len(mat[0]) != 1:
                self.diagonaltraversal(array,mat,i,j+1,p+1,0)
            else:
                self.diagonaltraversal(array,mat,i+1,j,p+1,0)
        elif i==0 and 0<j<len(mat[0])-1 and d==0:
            array[p]=mat[i][j]
            self.diagonaltraversal(array,mat,i+1,j-1,p+1,0)
        elif i==0 and 0<j<len(mat[0])-1 and d==1:
            array[p]=mat[i][j]
            self.diagonaltraversal(array,mat,i,j+1,p+1,0)
        elif 0<i<len(mat)-1 and j==0 and d==0:
            array[p]=mat[i][j]
            self.diagonaltraversal(array,mat,i+1,j,p+1,1)
        elif 0<i<len(mat)-1 and j==0 and d==1:
            array[p]=mat[i][j]
            self.diagonaltraversal(array,mat,i-1,j+1,p+1,1)
        elif i==len(mat)-1 and d==0:
            array[p]=mat[i][j]
            self.diagonaltraversal(array,mat,i,j+1,p+1,1)
        elif i==len(mat)-1 and d==1:
            array[p]=mat[i][j]
            self.diagonaltraversal(array,mat,i-1,j+1,p+1,1)
        elif j==len(mat[0])-1 and d==0:
            array[p]=mat[i][j]
            self.diagonaltraversal(array,mat,i+1,j-1,p+1,0)
        elif j==len(mat[0])-1 and d==1:
            array[p]=mat[i][j]
            self.diagonaltraversal(array,mat,i+1,j,p+1,0) 
        elif 0<i<len(mat)-1 and 0<j<len(mat[0])-1 and d==0:
            array[p]=mat[i][j]
            self.diagonaltraversal(array,mat,i+1,j-1,p+1,0) 
        elif 0<i<len(mat)-1 and 0<j<len(mat[0])-1 and d==1:
            array[p]=mat[i][j]
            self.diagonaltraversal(array,mat,i-1,j+1,p+1,1) 
solution=Solution()
mat=[[6,9,7]]
a=solution.findDiagonalOrder(mat)
print(a)