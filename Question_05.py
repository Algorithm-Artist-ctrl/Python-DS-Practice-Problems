def reverse_list(lst):
    return f"Before Reversing list {lst} after Reverse list is {lst[::-1]}"
usr_input=input("Enter the numbers separeted by spaces :\n")
usr_list=list(map(int,usr_input.split()))
print(reverse_list(usr_list))