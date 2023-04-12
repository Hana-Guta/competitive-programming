class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        nums.sort()
        for i in range(1,len(nums)-1):
            if (nums[i-1] + nums[i+1])/ 2 == nums[i]:
                for j in range(len(nums)):
                    if (nums[i-1] + nums[i+1]) / 2 != nums[j]: 
                        nums[i],nums[j] = nums[j] ,nums[i]
                        break
        return nums
                
        
