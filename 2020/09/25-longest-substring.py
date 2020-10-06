def can_move_forward(front_char, distinct_characters, k):
    character_set = distinct_characters.keys()
    return front_char in character_set or len(character_set) < k


def longest_substring_with_k_distinct_characters(s, k):
    if len(s) <= k:
        return len(s)

    max_count = 0
    fast_pointer = 0
    slow_pointer = 0
    distinct_characters = {}

    while fast_pointer < len(s):
        front_char = s[fast_pointer]
        rear_char = s[slow_pointer]

        if can_move_forward(front_char, distinct_characters, k):
            distinct_characters[front_char] = distinct_characters.get(front_char, 0) + 1
            fast_pointer += 1
        else:
            slow_pointer += 1
            distinct_characters[rear_char] -= 1
            if not distinct_characters[rear_char]:
                del distinct_characters[rear_char]

        max_count = max(max_count, fast_pointer - slow_pointer)

    return max_count


print(longest_substring_with_k_distinct_characters('aabcdefff', 3))
# 5 (because 'defff' has length 5 with 3 characters)
