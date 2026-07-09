from typing import List

def get_last_three_elements(my_list: List[int]) -> List[int]:
    if len(my_list) == 3:
        last_3_elts = my_list
    else:
        last_3_elts = my_list[-3:]
    return last_3_elts 


# do not modify below this line
print(get_last_three_elements([1, 2, 3]))
print(get_last_three_elements([1, 2, 3, 4, 5]))
print(get_last_three_elements([1, 2, 3, 4, 5, 6, 7, 8, 9]))