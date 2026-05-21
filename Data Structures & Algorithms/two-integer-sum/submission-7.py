class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        complements = {}
        for idx, num in enumerate(nums):
            looking = target - num
            if looking in complements:                
                return [complements[looking], idx]
            complements[num] = idx
        return []