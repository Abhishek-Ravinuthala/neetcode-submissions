class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + '*' + s
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        r = 0
        while r<len(s):
            start = r
            while s[r]!='*':
                r+=1

            length = int(s[start:r])
            string = s[r+1 : r+1+length]
            r = r+1+length
            res.append(string)
        return res
            
