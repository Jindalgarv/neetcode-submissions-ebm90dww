class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mp=Counter(nums)
        sorted_mp=sorted(mp.items(),key=lambda x: x[1],reverse= True )
        return [x[0] for x in sorted_mp[:k]]
