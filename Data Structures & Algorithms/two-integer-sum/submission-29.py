class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numsHash = {}

        for i, n in enumerate(nums):
            diff = target - n
            if diff in numsHash:
                return [numsHash[diff], i]
            
            numsHash[n] = i