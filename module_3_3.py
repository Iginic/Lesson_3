def print_params(a=1, b='строка',c=True):
    print(a,b,c)

# часть 1
print_params()
print_params(b=25)
print_params(c=[1,2,3])
print_params(False,[1,34], 'ee') # все работает нормально

# часть 2
values_list = [555,12.3,[11,22]]
values_dict = {'a':999 ,'b':[88,45] ,'c': False}
print_params(*values_list)
print_params(**values_dict)  # все работает нормально

# часть 3
values_list_2 = [54.32, 'строка2']
print_params(*values_list_2,42)  # все работает нормально
