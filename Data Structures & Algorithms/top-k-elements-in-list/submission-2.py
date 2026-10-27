class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashMap = {}
        for i in nums:
            hashMap[i] = 1+hashMap.get(i, 0)
        

        bucket = [[] for _ in range(len(nums)+1)]
        for ele, count in hashMap.items():
            bucket[count].append(ele)
        
        res = []
        for i in range(len(nums), -1, -1):
            listOfEle = bucket[i]
            for j in range(len(listOfEle)):
                res.append(listOfEle[j])
                if len(res)==k:
                    return res
            

