class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        res = nums[0]
        
        while l <= r:
            # Subarray is sorted and this finds the minimum
            if nums[l] < nums[r]:
                res = min (res, nums[l])
                break
            
            m = (l+r) // 2
            #This ensures that if m is the right of pivot, it is stored
            res = min(res, nums[m])
            if nums[m] >= nums[l]:
                #Search right
                l = m + 1
            else:
                #Search left
                r = m - 1
        
        return res
