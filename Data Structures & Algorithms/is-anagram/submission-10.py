class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        letters = {}

        for c in s:            
            letters[c] = letters.get(c,0) + 1
            

        for d in t:
            if d in letters:
                letters[d] = letters.get(d,0) - 1
        
        return all(v == 0 for v in letters.values())

    