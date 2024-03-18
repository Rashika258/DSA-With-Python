class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # d = {}

        # for i, n in enumerate(nums):
        #     if n in d and abs(i-d[n]) <= k:
        #         return True
        #     else:
        #         d[n] = i

        # return False
        if k == 0:
            return False
        
        slidingWindow = set()

        for i in range(0, len(nums)):
            if nums[i] in slidingWindow:
                return True
            
            if i >= k:
                slidingWindow.remove(nums[i- k])
            slidingWindow.add(nums[i])
        
        return False
        