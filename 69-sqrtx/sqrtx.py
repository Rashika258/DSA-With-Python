class Solution:
    def mySqrt(self, x: int) -> int:
        left, right = 1, x
        while left <= right:
            mid = (left+right)//2
            if mid * mid == x:
                return mid
            if mid * mid > x:
                right = mid - 1
            else:
                left = mid + 1
        return right
        # if x==0 or x == 1:
        #     return x
        # for i in range(0, x+1):
        #     if i *i > x:
        #         return i - 1
        # num = 1
        # while num*num <= x:
        #     num+=1
        # return num
        