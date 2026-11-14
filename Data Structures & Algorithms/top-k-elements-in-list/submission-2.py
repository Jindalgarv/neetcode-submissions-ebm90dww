class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n=len(nums)
        freq=Counter(nums)
        output=[]
        bucket=[[] for _ in range(n+1)]
        for key,value in freq.items():
            bucket[value].append(key)
        for i in range(n,-1,-1):
            for num in bucket[i]:
                output.append(num)
                if len(output)==k:
                    return output
        