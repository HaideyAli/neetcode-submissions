class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = []
        for n in nums:
            if n in seen:
                continue
            else:
                seen.append(n)
        
        seen.sort()
        print(seen)
        
        if len(seen) == 0:
            return 0

        maxCount = 1
        count = 1
        for i in range(1, len(seen)):
            
            if seen[i] == seen[i-1]+1:
                count += 1
            else:
                maxCount = max(maxCount, count)
                count = 1
        
        maxCount = max(maxCount, count)

        return maxCount
