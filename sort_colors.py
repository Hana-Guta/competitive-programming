class Solution:
    def sortColors(self, nums: List[int]) -> None:
        zeros = nums.count(0)
        ones = nums.count(1)
        twos = nums.count(2)
        
        nums.clear()
        for i in range(zeros):
            nums.append(0)
        for j in range(ones):
            nums.append(1)
        for k in range(twos):
            nums.append(2)
        
        return nums
