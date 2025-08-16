def count_even_odd(lst):
    count_even=0
    count_odd=0
    for i in lst:
        if i%2==0:
            count_even+=1
        else:
            count_odd+=1
    return f"Total Number of even is {count_even} and Odd is {count_odd}"
usr_input=input("Enter the number separeted by space:\n")
usr_list=list(map(int,usr_input.split()))
print(count_even_odd(usr_list))