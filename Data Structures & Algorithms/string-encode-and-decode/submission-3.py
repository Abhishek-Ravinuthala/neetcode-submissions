class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for i in strs:
            encoded += str(len(i)) + '*' + i
        return encoded

    def decode(self, s: str) -> List[str]:
        i=0
        strs = []
        print(s)
        while i<len(s):
            index = i
            while s[i]!='*':
                i+=1
            length = int(s[index: i])
            strs.append(s[i+1:i+length+1])
            i=i+length+1
        return strs



