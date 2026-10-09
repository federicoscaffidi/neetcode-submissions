class Solution:
    def isPalindrome(self, s: str) -> bool:
        ascii_alpha = list(range(65,91)) + list(range(97,123)) + list(range(48,58))
        left, right = 0, len(s) - 1
        while left < right:
            print(s[left], s[right])
            print(ord(s[left]), ord(s[right]))
            if ord(s[left]) not in ascii_alpha:
                left += 1
                continue
            if ord(s[right]) not in ascii_alpha:
                right -= 1
                continue
            print(left, right)
            print(s[left], s[right])
            if s[left].lower() != s[right].lower():
                return False
            left += 1
            right -= 1
        return True

