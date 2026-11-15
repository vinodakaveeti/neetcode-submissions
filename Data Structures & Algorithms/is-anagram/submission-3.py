class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        anagram_d = {}
        if len(s) != len(t):
            return False
        for v in s:
            anagram_d[v] = anagram_d.get(v, 0) + 1
        
        for v2 in t:
            if v2 not in anagram_d or anagram_d[v2] <= 0:
                return False
            else:    
                anagram_d[v2] -= 1
        return True
        