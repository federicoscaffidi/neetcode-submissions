class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == "":
            return 0
        left = 0
        right = 1
        length = 1
        char_set = set(s)
        mem = set(s[left])
        while left <= right and right < len(s) and length < len(char_set):
            if s[right] not in mem:
                length = max(length, len(s[left:right+1]))
                mem.add(s[right])
            else:
                mem.remove(s[left])
                left += 1
                continue
            right += 1
        return length