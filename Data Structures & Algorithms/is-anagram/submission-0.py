class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        freq_s = {}
        freq_t = {}

        for char_s in s:
            if char_s in freq_s:
                freq_s[char_s] += 1
            else:
                freq_s[char_s] = 1

        for char_t in t:
            if char_t in freq_t:
                freq_t[char_t] += 1
            else:
                freq_t[char_t] = 1  

        if freq_s == freq_t:
            return True

        return False