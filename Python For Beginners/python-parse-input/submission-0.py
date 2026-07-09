from typing import List

def read_integers() -> List[int]:
    user_input = input("")
    output = user_input.split(",")
    res = []
    for val in output:
        res.append(int(val))
    return res

# do not modify the code below
print(read_integers())
print(read_integers())
print(read_integers())
