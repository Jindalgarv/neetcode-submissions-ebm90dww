class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s=set(nums)
        longest=0
        for num in nums:
            if num-1 not in s:
                k=0
                while num+k in s:
                    longest=max(longest,k+1)
                    k+=1
        return longest