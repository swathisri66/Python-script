#dictionaries

D = {'name': 'swathi', 'age': 36, 'year': 1984}
print(D)
print(D['name'])

E = {'name': 'Kamani', 15: 34, True: True, (2,3): 9}
print(E[(2,3)])

print(len(E))
print(D.get('name'))

D.update({'name':'swathi'})
print(D)
D.keys()
dict_keys(['name', 'year', 'age'])

D.values()
dict_values(['swathi','2000',36])

D.items()
print(D)
dict_items([('name', 'max'), ('year', 2000), ('age', 36)])
D.popitem()
