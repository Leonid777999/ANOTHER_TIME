dictionary = {
    'name': 'Paul',
    'surname': 'Jones',
    'age': 35
    }

print(dictionary['name'], dictionary['age'])
print(dictionary.keys())
print(dictionary.values())

dictionary['age'] = 45
print(dictionary.values())

dictionary.update({'maritalStatus': 'single'})
print(dictionary)

dictionary.update({'children': ['Jack', 'Bill', 'John']})
print(dictionary['name'], dictionary['children'])

del dictionary['age']
print(dictionary)

print(dictionary.pop('name'))
print(dictionary)

################-tuple-############################
tuple = (1, 'number', 1.234, [1,2,3], -11, 'items', 0.56655, 'freaks', {'diction': 1,'diction2': 2}, 'bimber')
tuple1 = ('dfgdfgdffgdfgdf', 'dfgdfgdfgdfgdfgdfgdfgfdgdfgfdgffdgd')

print(tuple)
print(tuple[-4:])
print(tuple.index('items'))

print(tuple+tuple1)

(first_tuple, second_tuple, third_tuple, *other_tuples) = tuple
print(first_tuple)
print(second_tuple)
print(third_tuple)
print(other_tuples)




