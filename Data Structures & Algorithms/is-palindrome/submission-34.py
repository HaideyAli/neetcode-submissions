class Solution:
    def isPalindrome(self, s: str) -> bool:
        loweredText = s.lower()
        l = 0
        r = len(loweredText) - 1

        while l < r:
            if not self.isAlphaNum(loweredText[l]):
                l += 1
                continue
            
            if not self.isAlphaNum(loweredText[r]):
                r -= 1
                continue
            
            if loweredText[l] != loweredText[r]:
                print(loweredText[l], loweredText[r])
                return False
            
            l += 1
            r -= 1
        
        return True

    def isAlphaNum(self, c):
        return (ord('a') <= ord(c) <= ord('z') or
            ord('0') <= ord(c) <= ord('9'))
    