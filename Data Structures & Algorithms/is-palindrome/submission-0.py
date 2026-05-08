class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_Str = ""
        for ch in s:
            if ch.isalnum():
                new_Str += ch.lower()
        return new_Str == new_Str[::-1]