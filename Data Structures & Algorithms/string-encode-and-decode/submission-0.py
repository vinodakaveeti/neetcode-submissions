class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        for s in strs:
            result += str(len(s))+'#'+s
        return result

    def decode(self, s: str) -> List[str]:
        i = 0
        res = []
        while i < len(s):
            j = i

            while s[j] != '#':
                j += 1

            s_l = int(s[i:j])
            word = s[j+1: j+s_l+1]
            res.append(word)
            i = j+s_l+1

        return res