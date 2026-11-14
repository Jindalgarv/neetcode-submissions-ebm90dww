class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l,r=0,0
        max_len=0
        seen=set()
        while r<len(s):
            if s[r] not in seen:
                seen.add(s[r])
                max_len=max(max_len,len(seen))
                r+=1
            else:
                seen.remove(s[l])
                l+=1
        return max_len