class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        arr=sorted([int(i) for i in nums])
        arr.sort(reverse=True) 
        return str(arr[k-1])
          
        
                
       
