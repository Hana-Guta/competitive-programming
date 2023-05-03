class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        counter = 1
        while counter < n:
            counter *= 4
        return counter == n
