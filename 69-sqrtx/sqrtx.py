class Solution:
    def mySqrt(self, x: int) -> int:
        if x==0 or x == 1:
            return x
        for i in range(0, x+1):
            if i *i > x:
                return i - 1
        # num = 1
        # while num*num <= x:
        #     num+=1
        # return num
        