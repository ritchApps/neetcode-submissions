class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)
        for word in strs:
            sortWord = "".join(sorted(word))
            result[sortWord].append(word)
        return list(result.values())
        #     words = []
        #     if sortWord in grouping:
        #         words = grouping[sortWord]
        #         words.append(word)
        #         grouping[sortWord] = words
        #     else:
        #         grouping[sortWord] = [word]
        # result = []
        # for group in grouping:
        #     result.append(grouping[group])

        # return result