class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = [[] for _ in range(len(nums)+1)]
        output = []
        Map = {}
        for i in nums:
            Map[i] = 1 + Map.get(i, 0)
        
        for i, c in Map.items():
            res[c].append(i)

        i=len(nums)
        while i>=0 and k>0:
            array = res[i]
            for x in array:
                if k==0:
                    break
                output.append(x)
                k-=1
            i-=1
        return output
            