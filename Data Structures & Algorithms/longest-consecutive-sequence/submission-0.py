class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hash = set(nums)
        starts = set()
        maxCount = 0
        for n in hash:
            if n-1 not in hash:
                count = 1
                while n+count in hash: count+=1
                maxCount = max(maxCount, count)
        return maxCount