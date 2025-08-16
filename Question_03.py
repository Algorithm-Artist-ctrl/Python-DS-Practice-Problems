def remove_duplicates(lst):
    dup=set(lst)
    rem=list(dup)
    return f"After removing dupilicate elements from {lst} is {rem}"
usr_input=input("Enter the numbers separeted by space:\n")
usr_list=list(map(int,usr_input.split()))
print(remove_duplicates(usr_list))