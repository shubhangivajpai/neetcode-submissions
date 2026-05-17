class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        dict1 = {}
        for i,num in enumerate(numbers, start=1):
            diff = target-num

            if diff in dict1:
                return [dict1[diff],i]
            dict1[num] = i