class Solution:
    def naiveLengthOfLongestSubstring(self, s):
        if not len(s):
            return 0
        if len(s) == 1:
            return 1
        characters = set()
        counter = 0
        for char in s:
            if char not in characters:
                characters.add(char)
                counter += 1
            else:
                break
        return max(counter, self.naiveLengthOfLongestSubstring(s[1:]))


print(Solution().naiveLengthOfLongestSubstring('abrkaabcdefghijjxxx'))
