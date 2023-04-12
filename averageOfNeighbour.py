class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        def swap(l, r):
            nums[l], nums[r] = nums[r], nums[l]
        for i in range(1, len(nums)-1):
            num1 = nums[i-1]
            num = nums[i]
            num2 = nums[i+1]
            if num1 < num < num2 or num1 > num > num2:
                swap(i+1, i)
        return nums
