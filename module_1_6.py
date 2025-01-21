my_dict = {'Radmila' : 1987, 'Zarina' : 2012, 'Hasan' : 2014, 'Amir' : 2020}
print(f'Dict: {my_dict}')
print(f'Existing value: {my_dict['Hasan']}')
print(f'Not existing value: {my_dict.get('Karina')}')
my_dict.update({'Regina' : 1989, 'Dinar' : 1986})
get_person = my_dict.pop('Radmila')
print(f'Deleted value: {get_person}')
print(f'Modified dictionary: {my_dict}')
print()
my_set = {1, 2, 3, "Phyton", 44.44, False, True, 3, 2, 1, "Phyton"}
print(f'Set: {my_set}')
my_set.add((4, 5, 5.5))
my_set.add("Git")
print(f'Modified set: {my_set}')
