# Python dictionaries are implemented as hash tables with a standard O(1) lookup, insertion, deletion, and access.

hash_table = dict()
hash_table = {1: 'one', 2: 'two', 3: 'three', 4: 'four'}
print(hash_table)

print(hash_table.keys())

print(hash_table.values())

print(hash_table.items())

print(hash_table[1]) # accessing a value by its key -> O(1)

hash_table[5] = 'five' # inserting a value -> O(1)

del hash_table[4] # deleting a value -> O(1)

print('five' in hash_table.values()) # searching for a value -> O(1)

print(hash_table)