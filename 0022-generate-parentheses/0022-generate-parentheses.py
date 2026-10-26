from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def backtrack(s: str, openCount: int, closeCount: int):
            if len(s) == 2 * n:
                res.append(s)
                return

            if openCount < n:
                backtrack(s + "(", openCount + 1, closeCount)

            if closeCount < openCount:
                backtrack(s + ")", openCount, closeCount + 1)

        backtrack("", 0, 0)
        return res