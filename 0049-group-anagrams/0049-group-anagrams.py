class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anag = defaultdict(list)
        for s in strs:
            anag[tuple(sorted(s))].append(s)
        return list(anag.values())