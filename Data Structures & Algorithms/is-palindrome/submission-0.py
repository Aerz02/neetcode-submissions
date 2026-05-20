class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleanS = "".join(char for char in s.lower() if char.isalnum())
        print(cleanS)
        l, r = 0, len(cleanS) - 1
        while(l < r):
            if (cleanS[l] != cleanS[r]):
                return False
            l += 1
            r -= 1
        return True