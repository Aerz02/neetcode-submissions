class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        count_s, count_t = {}, {}
        for r in range(len(s)):
            count_s[s[r]] = count_s.get(s[r], 0) + 1
            count_t[t[r]] = count_t.get(t[r], 0) + 1
        for n in count_s:
            if count_s[n] != count_t.get(n, 0):
                return False
        return True