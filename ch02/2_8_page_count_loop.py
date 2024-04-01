# list of numbers
my_list_of_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

total_sum = 0

for a_number in my_list_of_numbers:
    total_sum += a_number

# for a_number_2 in my_list_of_numbers:
    # total_sum += a_number # NameError: name 'a_number' is not defined

print(f"Total sum of numbers in the list: {total_sum}")