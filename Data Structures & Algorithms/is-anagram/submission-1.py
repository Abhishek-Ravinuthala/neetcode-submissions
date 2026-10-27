class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t): return False
        charS, charT = {}, {}
        for i in s:
            charS[i] = 1+charS.get(i, 0)
        for c in t:
            charT[c] = 1+charT.get(c, 0)
        return charS==charT
        
