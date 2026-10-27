class Solution:

    def encode(self, strs: List[str]) -> str:
        
        encoded = ""
        for string in strs:
            encoded += str(len(string)) + '*' + string
        return encoded


    def decode(self, s: str) -> List[str]:
        strings = []
        i = 0
        while i<len(s):
            start = i
            while i<len(s) and s[i]!='*':
                i+=1
            length = int(s[start:i])
            strings.append(s[i+1:i+1+(length)])
            i=i+length+1
        return strings
            
            
