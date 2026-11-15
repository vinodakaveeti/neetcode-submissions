import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = {}
        queue = []

        for v in nums:
            res[v] = res.get(v, 0) + 1

        for (ki, v) in res.items():
            heapq.heappush(queue, (v, ki))

            if len(queue) > k:
                heapq.heappop(queue)

        return [v for ki,v in queue]


        