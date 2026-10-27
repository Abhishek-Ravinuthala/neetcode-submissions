class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ''
        for s in strs:
            encoded += str(len(s)) + '*' + s
        return encoded
        

    def decode(self, s: str) -> List[str]:
        res = []
        i=0
        while i<len(s):
            drift = i
            while s[i]!='*' and i<len(s):
                i+=1
            length = int(s[drift:i])
            res.append(s[i+1:i+1+length])
            i=i+length+1
        return res

            

            
