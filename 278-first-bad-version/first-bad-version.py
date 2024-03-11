# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        # i= 1
        # j=n
        # while (i < j):
        #     pivot = (i+j) //2
        #     if(isBadVersion(pivot)):
        #         j = pivot
        #     else:
        #         i = pivot +1
        # return i

        left,right = 0, n
        mid = n // 2
        while left < right:
            if isBadVersion(mid):
                right = mid
            else:
                left = mid + 1
            mid = (left + right) // 2
        return left


        