def merge_two_sorted_lists(list1, list2):
    list1.sort()
    list2.sort()
    merge=list1+list2
    return f"After sorting both list is {merge}"
usr_input_1=input("Enter the numbers of list 1 separeted by spaces:\n")
usr_input_2=input("Enter the numbers of list 2 separeted by spaces:\n")
usr_list_1=list(map(int,usr_input_1.split()))
usr_list_2=list(map(int,usr_input_2.split()))
print(merge_two_sorted_lists(usr_list_1,usr_list_2))