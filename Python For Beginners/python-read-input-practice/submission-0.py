def add_two_numbers() -> int:
    elts = input()
    elts = elts.split(",")
    sum_elts = 0
    for elt in elts:
        elt = int(elt) 
        sum_elts = sum_elts + elt
    return sum_elts

# do not modify below this line
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
