class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        freq_map={}
        for num in nums1:
            freq_map[num] = freq_map.get(num, 0)+1
        
        res = []
        for num in nums2:
            if num in freq_map and freq_map[num] > 0:
                res.append(num)
                freq_map[num]-=1

        return res