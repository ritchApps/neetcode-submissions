class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        grouping = {}
        for word in strs:
            sortWord = "".join(sorted(word))
            words = []
            if sortWord in grouping:
                words = grouping[sortWord]
                words.append(word)
                grouping[sortWord] = words
            else:
                grouping[sortWord] = [word]
        result = []
        for group in grouping:
            result.append(grouping[group])

        return result