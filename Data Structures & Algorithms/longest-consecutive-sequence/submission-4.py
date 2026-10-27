class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashSet = set(nums)
        res = 0
        for i in hashSet:
            if i-1 not in hashSet:
                count = 1
                while i+count in hashSet:
                    count+=1
                res = max(res, count)
        return res

            