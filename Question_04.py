def check_unique(lst):
    unq=set(lst)
    lst_2=list(unq)
    if lst_2==lst:
        return True
    else:
        return False
usr_input=input("Enter the numbers separeted by space:\n")
usr_list=list(map(int,usr_input.split()))
print(check_unique(usr_list))