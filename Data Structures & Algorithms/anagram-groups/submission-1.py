class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashMap = defaultdict(list)
        for s in strs:
            char = [0] * 26
            for c in s:
                char[ord(c) - ord('a')] +=1
            hashMap[tuple(char)].append(s)
        return list(hashMap.values())
            