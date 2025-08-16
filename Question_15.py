def is_subset(lst1, lst2):
    set1=set(lst1)
    set2=set(lst2)
    return set1.issubset(set2)
usr_input_1=input("Enter the numbers of list 1 separeted by spaces:\n")
usr_input_2=input("Enter the numbers of list 2 separeted by spaces:\n")
usr_list_1=list(map(int,usr_input_1.split()))
usr_list_2=list(map(int,usr_input_2.split()))
print(is_subset(usr_list_1,usr_list_2))
