class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        l=0
        r = len(numbers)-1
        curr_sum =0

        while l<r:
            curr_sum = numbers[l]+numbers[r]

            if curr_sum>target:
                r-=1
            elif curr_sum < target:
                l+=1
            else:
                return [l+1,r+1]
        return []

        # dict1 = {}
        # for i,num in enumerate(numbers, start=1):
        #     diff = target-num

        #     if diff in dict1:
        #         return [dict1[diff],i]
        #     dict1[num] = i