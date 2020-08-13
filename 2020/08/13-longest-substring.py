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

    def slidingLengthOfLongestSubstring(self, s):
        if not len(s):
            return 0
        if len(s) == 1:
            return 1
        characters = set(s[0])
        slow_runner = 0
        fast_runner = 1
        max_len = 0
        while fast_runner < len(s):
            if s[fast_runner] in characters:
                characters.remove(s[slow_runner])
                slow_runner += 1
            else:
                characters.add(s[fast_runner])
                fast_runner += 1
            max_len = max(max_len, fast_runner - slow_runner)
        return max_len


print(Solution().slidingLengthOfLongestSubstring('abrkaabcdefghijklmjabcdefghijklmnopxxx'))
