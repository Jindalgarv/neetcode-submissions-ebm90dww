class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        piles.sort(reverse=True)
        m=piles[0]
        l,r=1,m
        time,t=0,0
        while l<=r:
            mid=l+(r-l)//2
            t=0
            for i in piles:
                t+=math.ceil(i/mid)
            if t<=h:
                r=mid-1
            else:
                l=mid+1
        return l
            
        
        