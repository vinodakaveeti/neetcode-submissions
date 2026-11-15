import heapq
class Solution:
    def topKFrequent(self, nums: List[int], t: int) -> List[int]:
        res = {}

        for v in nums:
            res[v] = res.get(v, 0) + 1

        res_list = [[] for _ in range(len(nums)+1)]

        for k, v in res.items():
            res_list[v].append(k)
        res_final = []

        for v in res_list[::-1]:

            if t == 0:
                return res_final

            if v != []:
                for r in v:
                    res_final.append(r)
                    t -= 1

        return