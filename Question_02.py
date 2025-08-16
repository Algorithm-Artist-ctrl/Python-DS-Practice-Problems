import math
def find_largest(numbers):
    max=0
    for i in numbers:
        if i>=max:
            max=i
    return f"Largest number in {numbers} is {max}" 
usr_input=input("Enter numbers separated by space:\n")
usr_list=list(map(int,usr_input.split()))
print(find_largest(usr_list))