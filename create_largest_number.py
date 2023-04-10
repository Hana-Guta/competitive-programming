class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        num = [str(i) for i in nums]
        count = ""
        while len(num) > 0:
            i = 0
            while i < len(num):
                num_idx = num[i]
                for j in num:
                    if num_idx + j < j + num_idx:
                        num_idx = j
                num.remove(num_idx)
                count += num_idx
        return str(int(count))
