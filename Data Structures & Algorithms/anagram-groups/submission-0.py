class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        res_d  = {}

        for v in strs:
            s_v = ''.join(sorted(v))
            if s_v in res_d:
                res_d[s_v].append(v)
            else:
                res_d[s_v] = [v]

        return list(res_d.values())
        