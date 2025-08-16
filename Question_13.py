def is_palindromic_tuple(tup):
    rev=tup[::-1]
    if rev==tup:
        print("Pallindrome Tuple")
    else:
        print("Not Pallindrome")
usr_input=input("Enter numbers separeted by spaces:\n")
usr_tuple=tuple(map(int,usr_input.split()))
is_palindromic_tuple(usr_tuple)