class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = defaultdict(list)

        for s in strs:
            characters = [0] * 26
            
            for l in s:
                index = ord(l) - ord('a')
                characters[index] += 1
            
            group[tuple(characters)].append(s)

        return list(group.values())