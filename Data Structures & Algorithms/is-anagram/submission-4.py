class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        lettersInS = {}
        lettersInT = {}

        for c in s:
            if c in lettersInS:
                lettersInS[c] += 1
            else:
                lettersInS[c] = 1

        for d in t:
            if d in lettersInT:
                lettersInT[d] +=1
            else:
                lettersInT[d] = 1
            
        return lettersInS == lettersInT
    