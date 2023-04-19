class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        ans = 0
        n = len(piles)
        # if n==3:
        #     return piles[1]
        for i in range(n - 2, n // 3 - 1, -2):
            ans += piles[i]
        return ans
