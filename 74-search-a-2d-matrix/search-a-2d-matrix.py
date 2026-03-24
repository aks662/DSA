class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l=0
        h=len(matrix)-1
        ans=False
        while l<=h:
            mid=(l+h)//2
            
            if matrix[mid][0]>target:
                h=mid-1
            elif matrix[mid][-1]<target:
                l=mid+1
                
            else:
                l1=0
                h1=len(matrix[mid])-1
                while l1<=h1:
                    
                    mid1=(l1+h1)//2
                    if matrix[mid][mid1]==target:
                        ans=True
                        # print(True)
                        break
                    elif  matrix[mid][mid1]>target:
                        h1=mid1-1
                    else:
                        l1=mid1+1
                        
                break
        return (ans) 