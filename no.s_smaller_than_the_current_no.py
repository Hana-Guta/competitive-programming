class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        arr = sorted(nums)
        array=[]
        for i in nums:
            idx=arr.index(i)
            array.append(idx)
        return array
