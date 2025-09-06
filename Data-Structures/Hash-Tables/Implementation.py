# Implementation of Hash Table data structure.

class HashTable:
    def __init__(self, size):
        self.size = size
        self.data = [None]*self.size # initializing a list of given size

    def _hash(self, key): # very simple hashing function example - O(1) as hash functions are fast, despite looping over key
        hash = 0
        for i in range(len(key)):
            hash = (hash + ord(key[i])*i) % self.size # get unicode point of character key provided
        return hash
    
    def set(self, key, value): # O(1)
        address = self._hash(key) # get address of item in hash table using the hashing function
        if not self.data[address]: # if the address returned by the hash in our hash table is empty, insert into it the key and value
            self.data[address] = [[key, value]]
        else: # otherwise, append it onto the list/array at that address to resolve collisions
            self.data[address].append([key, value])
        print(self.data)

    def get(self, key): # O(1) if no collisions, can become O(n) due to growing list of collisions
        address = self._hash(key)
        current_bucket = self.data[address]
        if current_bucket: # check if given address in our hash table has data or not, return data if yes
            for i in range(len(current_bucket)):
                if current_bucket[i][0] == key: # check if key item in list of items matches given key to return correct element
                    return current_bucket[i][1] # return the value of the key item
        return None # if given address is empty, return None
    
    def keys(self):
        keys_array = []
        for i in range(len(self.data)):
            if self.data[i]: # check if the current position in the hash table has data
                if len(self.data[i]) > 1: # if the current position has multiple key items, loop over them to return all list keys
                    for j in range(len(self.data[i])):
                        keys_array.append(self.data[i][j][0])
                else:
                    keys_array.append(self.data[i][0][0])
        return keys_array
    
    def values(self):
        values_array = []
        for i in range(len(self.data)):
            if self.data[i]: # check if the current position in the hash table has data
                if len(self.data[i]) > 1: # if the current position has multiple key items, loop over them to return all list keys
                    for j in range(len(self.data[i])):
                        values_array.append(self.data[i][j][1])
                else:
                    values_array.append(self.data[i][0][1])
        return values_array

    

    
my_hashtable = HashTable(10)

# add items to hash table:
my_hashtable.set('tangerine', 10000)
my_hashtable.set('kiwi', 150)
my_hashtable.set('apples', 54) # causing a collision to happen

# get items from table:
print(my_hashtable.get('kiwi'))
print(my_hashtable.get('tangerine'))
print(my_hashtable.get('apples')) # item in list due to collision
print(my_hashtable.get('potatoes')) # empty item

# retrieve all keys in hash table:
print(my_hashtable.keys())

# retrieve all values in hash table:
print(my_hashtable.values())