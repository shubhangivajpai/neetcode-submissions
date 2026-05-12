class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict1 ={}
        for num in nums:
            if num in dict1:
                dict1[num]+=1
            else:
                dict1[num] = 1
        arr = []
        for key,val in dict1.items():
            arr.append([val,key])
        arr.sort()

        res = []

        while len(res)<k:
            res.append(arr.pop()[1])
        return res


        