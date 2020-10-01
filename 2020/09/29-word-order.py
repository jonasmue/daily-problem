def word_to_number(word, char_factor, max_factor):
    n = 0
    idx_factor = max_factor
    for char in word:
        n += idx_factor * char_factor[char]
        idx_factor = idx_factor // 10
    return n

def isSorted(words, order):
    if len(words) < 2:
        return True

    max_len = 0
    for word in words:
        max_len = max(max_len, len(word))
    char_factor = {v: k + 1 for k, v in enumerate(order)}
    max_factor = 10 ** (max_len - 1)
    last_word_number = 0
    for word in words:
        current_word_number = word_to_number(word, char_factor, max_factor)
        if current_word_number < last_word_number:
            return False
        last_word_number = current_word_number
    return True


print(isSorted(["abcd", "efgh"], "zyxwvutsrqponmlkjihgfedcba"))
# False
print(isSorted(["zyx", "zyxw", "zyxwy"],
               "zyxwvutsrqponmlkjihgfedcba"))
# True
print(isSorted(["hello", "latin"],
               "habcldefgijkmnopqrstuvwxyz"))
# True
print(isSorted(["word", "world", "row"],
               "abcworldefghijkmnpqstuvxyz"))
# False