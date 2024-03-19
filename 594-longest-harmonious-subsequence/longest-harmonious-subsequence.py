class Solution:
    def findLHS(self, nums: List[int]) -> int:
        n=len(nums)
        nums.sort()
        maxLen = 0
        i, j = 0, 1

        while i < n and j < n:
            if(nums[j] - nums[i]) == 1:
                maxLen = max(maxLen, j-i+1)
                j+=1
            
            elif (nums[j] - nums[i]) == 0:
                j+=1
            
            elif (nums[j] - nums[i]) > 1:
                i+=1

        return maxLen