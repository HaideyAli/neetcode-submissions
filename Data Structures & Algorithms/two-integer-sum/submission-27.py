class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numsHash = {}

        for i in range(len(nums)):
            numsHash[nums[i]] = i

        for i in range(len(nums)):
            val = target - nums[i]
            if val in numsHash and numsHash.get(val) != i:
                return [min(i, numsHash.get(val)), max(i, numsHash.get(val))]
        

