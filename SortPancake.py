class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        n = len(arr)
        res = []
        for i in range(n, 0, -1):
            j = arr.index(i)
            arr[:j+1] = arr[:j+1][::-1]
            arr[:i] = arr[:i][::-1]
            res.append(j+1)
            res.append(i)
        return res
