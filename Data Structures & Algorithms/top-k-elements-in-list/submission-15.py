class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        found = {}        
        result = []
        for num in sorted(nums):              
            found[num] = found.get(num,0) + 1
        sortFound = dict(
            sorted(found.items(), key=lambda item: item[1], reverse=True)
        )
        ordered_keys = list(sortFound.keys())
        for i in range(k):
            result.append(ordered_keys[i])
        
        
        return result