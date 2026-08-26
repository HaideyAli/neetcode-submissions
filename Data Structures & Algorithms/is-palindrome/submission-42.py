class Solution:
    def isPalindrome(self, s: str) -> bool:
        a = 0
        b = len(s) - 1

        newString = s.lower()


        while a < b:
            while a < b and not self.isAlphaNum(newString[a]):
                a += 1


            while b > a and not self.isAlphaNum(newString[b]):
                b -= 1

            if newString[a] != newString[b]:
                return False

            a += 1
            b -= 1
        
        return True

    def isAlphaNum(self, c):
        return (ord('a') <= ord(c) <= ord('z') or
            ord('0') <= ord(c) <= ord('9'))
    