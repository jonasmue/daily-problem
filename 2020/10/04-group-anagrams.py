import collections


def groupAnagramWords(strs):
    found_anagrams = {}
    grouped_anagrams = []
    for i, s in enumerate(strs):
        sorted_string = "".join(sorted(s))
        if sorted_string not in found_anagrams.keys():
            index = len(grouped_anagrams)
            found_anagrams[sorted_string] = index
            grouped_anagrams.append([s])
        else:
            grouped_anagrams[found_anagrams[sorted_string]].append(s)
    return grouped_anagrams


print(groupAnagramWords(['abc', 'bcd', 'cba', 'cbd', 'efg']))
# [['efg'], ['bcd', 'cbd'], ['abc', 'cba']]
