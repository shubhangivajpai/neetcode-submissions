class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict1 = {}
        for ch in s:
            dict1[ch] = dict1.get(ch,0)+1
        for ch in t:
            dict1[ch] = dict1.get(ch,0)-1
        for val in dict1.values():
            if val!=0:
                return False
        return True
        