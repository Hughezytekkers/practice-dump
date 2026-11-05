def chunk_list(lst, n):
    for i in range(0, len(lst), n):
        yield lst[i : i + n]


# Avoid naming variables after built-in types like 'list'
data = [1, 2, 3, 4, 5, 6, 7, 8]
n = 3

# Convert generator to a list for printing
print(f"the split up into chunks is: \n{list(chunk_list(data, n))}")