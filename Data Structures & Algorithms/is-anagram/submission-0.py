class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        counter = [0 for i in range(27)]
        for i in range(len(s)):
            counter[ord(s[i]) - 97] += 1
            counter[ord(t[i]) - 97] -= 1
        if counter == [0 for i in range(27)]:
            return True
        else:
            return False

        