class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sHash = {}
        tHash = {}

        for l in s:
            sHash[l] = 1 + sHash.get(l, 0)
        
        for l in t:
            tHash[l] = 1 + tHash.get(l, 0)

        if sHash == tHash:
            return True
        else:
            return False