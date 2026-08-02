class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)

        while l <= r:
            mid = (l + r) // 2

            hrs = 0
            for x in piles:
                hrs += (x + mid - 1) // mid

            if hrs <= h:
                r = mid - 1
            else:
                l = mid + 1

        return l