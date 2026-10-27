class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded=""
        for i in strs:
            i = str(len(i)) + '*'  + i
            encoded+=i
        # print(encoded)
        return encoded



    def decode(self, s: str) -> List[str]:
        decoded=[]
        i,j=0,0
        while i<len(s) and j<len(s):
            while s[j]!='*':
                j+=1
            length = int(s[i:j])
            i=j
            decoded.append(s[i+1: i+1+length])
            # print(decoded)
            i=i+length+1
            j=i
        return decoded


