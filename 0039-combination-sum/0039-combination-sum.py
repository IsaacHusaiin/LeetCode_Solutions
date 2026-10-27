class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        res = []
        def backtrack(start, current, remaining):
            if remaining == 0:                 
                res.append(current[:])
                return
            if remaining < 0:                
                return
            for i in range(start, len(candidates)):
                current.append(candidates[i])
                backtrack(i, current, remaining - candidates[i])  
                current.pop()                 
        backtrack(0, [], target)
        return res
        