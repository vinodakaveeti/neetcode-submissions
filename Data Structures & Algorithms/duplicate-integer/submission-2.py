from collections import Counter
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # if nums:
        #     sorted_list = list(Counter(nums).values())
        #     return sorted(sorted_list, reverse=True)[0]>=2
        # return False
        dup_dict = {}
        for v in nums:
            if v not in dup_dict:
                dup_dict[v]=1
            else:
                return True
        return False