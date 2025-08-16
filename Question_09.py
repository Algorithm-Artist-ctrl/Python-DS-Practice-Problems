def rotate_list(lst, k):
    n = len(lst)
    k = k % n  # Handle cases where k > length of list
    return lst[-k:] + lst[:-k]
print(rotate_list([1, 2, 3, 4, 5], 2))       # Output: [4, 5, 1, 2, 3]
print(rotate_list([10, 20, 30, 40, 50], 3))  # Output: [30, 40, 50, 10, 20]
