def max_consecutive_difference(lst):
    max_diff = 0
    for i in range(len(lst) - 2):
        num_1 = lst[i]
        num_2 = lst[i + 2]
        diff = abs(num_2 - num_1)
        if diff > max_diff:
            max_diff = diff
    print(max_diff)

usr_input = input("Enter the numbers separated by spaces:\n")
usr_list = list(map(int, usr_input.split()))
max_consecutive_difference(usr_list)
