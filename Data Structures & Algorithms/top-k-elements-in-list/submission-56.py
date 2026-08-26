class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        frequency = [[] for i in range(len(nums)+1)]

        for n in nums:
            count[n] = 1 + count.get(n, 0)
        
        for n, c in count.items():
            frequency[c].append(n)

        answer = []
        for i in range(len(nums), 0, -1):
            for n in frequency[i]:
                answer.append(n)
                if len(answer) == k:
                    return answer
        
        return answer