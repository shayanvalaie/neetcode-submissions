class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        
    
        maxNum = -1
#
        #[2,4,5,3,1,2]
         #maxNum = 2
         #n = -1

        for i in range(len(arr)-1, -1, -1):
            n = maxNum 
            maxNum = max(arr[i], maxNum)
            arr[i] = n
        return arr


