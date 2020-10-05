def is_valid(string):
    open = 0
    for char in string:
        if not open and char == ")":
            return False
        if char == "(":
            open += 1
        if char == ")":
            open -= 1
    return open == 0


def count_invalid_parenthesis(string):
    if is_valid(string):
        return 0
    minimum = len(string)
    for i, _ in enumerate(string):
        minimum = min(1 + count_invalid_parenthesis(string[:i] + string[i + 1:]), minimum)
    return minimum


print(count_invalid_parenthesis("()())()"))
# 1
