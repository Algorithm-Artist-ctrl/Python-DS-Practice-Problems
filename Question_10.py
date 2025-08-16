def merge_lists_to_dictionary(keys, values):
    result= dict(zip(keys,values))
    return f"After merging keys and values is {result}"
usr_key=input("Enter keys separeted by space;\n").split()
usr_values=input("Enter value separeted by space:\n")
usr_list=list(map(int,usr_values.split()))
print(merge_lists_to_dictionary(usr_key,usr_list))