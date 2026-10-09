class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        right = 0
        length = 0
        char_set = set(s)
        mem = set(s[left:right])
        while right < len(s) and length < len(char_set):
            if s[right] not in mem:
                length = max(length, right+1-left)
                mem.add(s[right])
                right += 1
            else:
                mem.remove(s[left])
                left += 1
        return length