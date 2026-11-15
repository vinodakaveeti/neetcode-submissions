from collections import Counter
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if nums:
            sorted_list = list(Counter(nums).values())
            return sorted(sorted_list, reverse=True)[0]>=2
        return False