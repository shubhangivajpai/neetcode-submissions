class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False
        # dict1 = {}
        # for num in nums:
        #     if num in dict1:
        #         dict1[num]+=1
        #     else:
        #         dict1[num]=1
        # for val in dict1.values():
        #     if val>1:
        #         return True
        # return False
        