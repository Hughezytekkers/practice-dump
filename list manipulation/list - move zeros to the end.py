# list where we will move zeros to the end

list = [0, 1, 0, 3, 12]


def move_zeros(lst):
    non_zeros = [item for item in lst if item != 0]
    zeros = [0] * (len(lst) - len(non_zeros))
    return non_zeros + zeros


print(f"The list with all the zeros moved is: \n{move_zeros(list)}")