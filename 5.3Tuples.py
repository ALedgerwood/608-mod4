# 5.3 Practice with Tuples

time_tuple = [9, 16, 1]
time_tuple
time_tuple[2]
time_tuple += (1, 6)
time_tuple

# modifying tuples using index

student_tuple = ('Alex', 'Green', [100, 89, 95])
student_tuple[2][1] = 99
student_tuple

single = (123.45,)
single

# getting error when trying to add a list to a tuple

[1, 2, 3] + (4, 5, 6)

# unpacking tuples

student_tuple = ('Alex', 'Green', [100, 89, 95])
first_name, fave_color, grades = student_tuple
grades

# creating a bar chart

numbers = [19, 3, 15, 7, 11]
print('nCreating a bar chart from numbers:')

print(f'Index{"Value":>8}   Bar')
    
for index, value in enumerate(numbers):
    print(f'{index:>5}{value:>8}   {"*" * value}')
    
