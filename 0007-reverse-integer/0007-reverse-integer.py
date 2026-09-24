class Solution:
    def reverse(self, x: int) -> int:

        sign=-1 if x<0 else 1 
        value = -2**31
        value2=2**31-1
        s = str(abs(x))[::-1]
        result = sign * int(s)
        if result < value or result > value2:
            return 0
        return result 