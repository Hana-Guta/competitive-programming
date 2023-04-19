class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        ans_arr = []
        for i in range(len(l)):
            subArr = nums[l[i]:r[i] + 1]
            subArr.sort()
            count = 0
            for j in range(1, len(subArr) - 1):
                if subArr[j] - subArr[j - 1] == subArr[-1] - subArr[-2]:
                    count += 1
                
            if count == len(subArr) - 2:
                ans_arr.append(True)
            else:
                ans_arr.append(False)
        return ans_arr
