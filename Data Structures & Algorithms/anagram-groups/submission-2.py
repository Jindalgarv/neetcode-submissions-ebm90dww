class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d=defaultdict(list)
        output=[]
        for s in strs:
            d[str(sorted(s))].append(s)
        for key,values in d.items():
            output.append(values)
        return output
        
        