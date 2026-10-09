class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == "":
            return 0
        left = 0
        right = 1
        length = 1
        char_set = set(s)
        mem = set(s[left])
        while right < len(s) and length < len(char_set):
            if s[right] not in mem:
                length = max(length, right+1-left)
                mem.add(s[right])
                right += 1
            else:
                mem.remove(s[left])
                left += 1
        return length