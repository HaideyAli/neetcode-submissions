class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dupset = set()

        for n in nums:
            if n in dupset:
                return True

            dupset.add(n)

        return False
            