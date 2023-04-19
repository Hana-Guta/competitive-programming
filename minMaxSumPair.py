class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        j = 0
        maximum = 0
        n = len(nums)
        for i in range(n - 1 , (n // 2) - 1 , -1):
            pair_sum= nums[j] + nums[i]
            maximum=max(maximum , pair_sum)
            j += 1
        return maximum
