#list rotation
def rotate_list(lst, k):
    if not lst:
        return lst
    k = k % len(lst) 
    return lst[-k:] + lst[:-k]


list = [0, 1, 0, 3, 12]
k = 2

print(f"the rotated list is: \n{rotate_list(list, k)}")