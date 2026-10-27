class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for i in strs:
            res+= str(len(i)) + '#' + i
        return res
    def decode(self, s: str) -> List[str]:
        res = []
        i,j = 0,0
        while i<len(s):
            
            while s[j]!='#':
                j+=1
            length = int(s[i:j])
            res.append(s[j+1 : length+j+1])
            i=length+j+1
            j=i
        return res

