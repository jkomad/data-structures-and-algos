"""  
1. Hash Table: Intro 

Python's built in hash table is dictionaries:
Structure:
- key 
- value 

Characteristics: 
    1. One way 
    2. Deterministic - For any particular hash function, we expect the same outcome every time

2. Collisions 

Occurs when you place a key, value pair in an address that already contains another key, value pair 

Separate Chaining = When you put a key, value pair at an address that already contains one ore more other key, value pairs 

Linear probing (open addressing) = another technique to search for an empty address to store an incoming key, value pair 

Separate chaining implementation can use linked lists instead of lists

3. Constructor 

The address space for a hash table should ideally use a prime number of addresses (reduces the number of potential collisions)

4. Big O  

Hash Method - O(1)
Set item - O(1) 
Get item - O(n), but the assumption of a hash table is that items are distributed randomly O(1)

5. Common Interview Question 

Given two lists, determine if the two share a common item. 

Approach 1 (Naive approach):
Nested for loops: 
    - 1 loop iterates through items in first list 
    - 2nd loop compares each item in the first list with each item in the second list
Run time complexity - O(n^2)

Approach 2(Hash table):
Create a dictionary(hash table) from the first list. 
Set each item as a key with value set to zero. 

Search for presence of key in dictionary (O(1))

Run time complexity - O(n)
"""


class HashTable:
    def __init__(self, size=7):
        self.data_map = [None] * size

    def __hash(self, key):
        my_hash = 0
        # hash each letter in key input
        for letter in key:
            my_hash = (my_hash + ord(letter) * 23) % len(self.data_map)
        return my_hash

    def set_item(self, key, value):
        # hash key
        index = self.__hash(key)
        # check existence of list at index in data map
        if self.data_map[index] is None:
            self.data_map[index] = []
        self.data_map[index].append([key, value])
        return

    def get_item(self, key):
        # hash key
        index = self.__hash(key)
        # check existence of key
        if self.data_map[index] is not None:
            item = [entry for entry in self.data_map[index] if entry[0] == key]
            return item[0][1]
        return None

    def keys(self):
        all_keys = []
        for item in self.data_map:
            if item is not None:
                for entry in item:
                    all_keys.append(entry[0])
        return all_keys

    def print_table(self):
        for i, v in enumerate(self.data_map):
            print(f"{i}:{v}")


if __name__ == "__main__":
    my_ht = HashTable()
    my_ht.set_item("nail", 1000)
    my_ht.set_item("bolts", 200)
    my_ht.set_item("washers", 50)
    my_ht.set_item("lumber", 70)
    print(my_ht.keys())
    my_ht.print_table()
