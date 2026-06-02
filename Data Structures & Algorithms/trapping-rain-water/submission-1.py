class Solution:
    def trap(self, height: List[int]) -> int:
        if not height: return 0

        l, r = 0, len(height) - 1
        leftMax, rightMax = height[l], height[r]

        res = 0

        while l < r:
            # This if essentially stops a negative number ever happening
            # because starting on the end with a low wall will always
            # mean that there HAS to be something to be gained from
            # maxL/R - height[l/r]
            if leftMax < rightMax:
                l += 1
                leftMax = max(leftMax, height[l])
                res += leftMax - height[l] #is never adding negatives
            else:
                r -= 1
                rightMax = max(rightMax, height[r])
                res += rightMax - height[r]

        return res