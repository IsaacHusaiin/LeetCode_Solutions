class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        pad = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl','6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        result =[""]
        for digit in digits:
            new_result = []
            for combo in result:
                for ch in pad[digit]:
                    new_result.append(combo+ch)
            result = new_result
        return result





