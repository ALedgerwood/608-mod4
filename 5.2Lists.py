# Lists
## practice with c integers

c = [-45, 6, 0, 72, 1543]
c
c[0]
c[4]
len(c)
c[-1]
c[100]
c[1] + c[2] + c[3]
c += 50
c[4] =+ 17

a_list = []
for number in range(1, 6):
    a_list =+ [number]
    
for number in range(1, 6):
    a_list += [number]
    
# practice concatenating lists

list1 = [10, 20, 30]
list2 = [40, 50]
concatenated_list = list1 + list2

concatenated_list
    
for i in range(len(concatenated_list)):
    print(f'{i}: {concatenated_list[i]}')
    
a = [1, 2, 3]
b = [1, 2, 3]
c = [1, 2, 3, 4]

c > b
a == b + c

def cube_list(values):
    for i in range(len(values)):
        values[i] **= 3
        
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
cube_list(numbers)
numbers

Alex Ledgerwood

get_ipython().run_line_magic('save', '')
