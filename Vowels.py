def Countit(tej):
    vowels = "aeiouAEIOU"
    count = 0
    for char in tej:  
        if char in vowels:
            count += 1
    return count

input_str = input("Enter a string: ")
print("The no. of vowels is:", Countit(input_str))
