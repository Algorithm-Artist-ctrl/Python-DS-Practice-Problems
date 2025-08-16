def sum_lst(numbers):
    sum=0
    for i in numbers:
        sum=sum+i
    return f"Sum of list Elements is {sum}"
# Take input like: 1 2 3 4 5
user_input = input("Enter numbers separated by spaces: ")
#print(user_input.split())

# Split the input string by spaces and convert each to int
user_list = list(map(int, user_input.split()))
print(sum_lst(user_list))
print(user_list)
