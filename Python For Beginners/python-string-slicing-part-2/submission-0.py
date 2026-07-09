def first_n_characters(s: str, n: int) -> str:
    if n < len(s):
        return s[:n]
    else:
        return s

def last_n_characters(s: str, n: int) -> str:
    if n < len(s):
        return s[len(s) - n:]
    else:
        return s

# do not modify below this line
print(first_n_characters("NeetCode", 3))
print(first_n_characters("NeetCode", 4))
print(first_n_characters("NeetCode", 8))

print(last_n_characters("NeetCode", 3))
print(last_n_characters("NeetCode", 4))
print(last_n_characters("NeetCode", 8))