class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res = {}
        for i, v in enumerate(nums):
            s = target - v
            if s in res:
                return [res[s], i]
            res[v] = i
        return 
        