# Hash Table Class
class HashTableChaining:
    def __init__(self, size=10):
        # Initialize table with empty lists for chaining
        self.size = size
        self.table = [[] for _ in range(size)]
    def hash_function(self, key):
        return hash(key) % self.size
    def insert(self, key, value):
        idx = self.hash_function(key)
        # Check if key already exists and update
        for pair in self.table[idx]:
            if pair[0] == key:
                pair[1] = value
                return
        # Otherwise, append new key-value pair
        self.table[idx].append([key, value])

    def search(self, key):
        """
        Search for a key in the hash table
        Return value if found, else None
        """
        idx = self.hash_function(key)
        for pair in self.table[idx]:
            if pair[0] == key:
                return pair[1]
        return None

    def delete(self, key):
        """
        Delete a key-value pair from the hash table
        Return True if deleted, False if not found
        """
        idx = self.hash_function(key)
        for i, pair in enumerate(self.table[idx]):
            if pair[0] == key:
                del self.table[idx][i]
                return True
        return False

    def __str__(self):
        """
        String representation of the hash table
        Shows each slot and its chained elements
        """
        table_str = ""
        for i, bucket in enumerate(self.table):
            table_str += f"Slot {i}: {bucket}\n"
        return table_str
def test_hash_table():
    # Initialize hash table
    ht = HashTableChaining(size=10)
    # Insert key-value pairs
    keys = ["apple", "banana", "orange", "grape", "pear"]
    values = [10, 20, 30, 40, 50]
    for k, v in zip(keys, values):
        ht.insert(k, v)
    print("Initial Hash Table:")
    print(ht)
    # Search examples
    print("Search 'orange':", ht.search("orange"))
    print("Search 'banana':", ht.search("banana"))
    print("Search 'kiwi':", ht.search("kiwi"))  # Key not present
    # Delete a key
    print("\nDeleting 'banana'...")
    ht.delete("banana")
    print("After deletion of 'banana':")
    print(ht)
    # Insert a new key
    print("\nInserting 'kiwi' = 60")
    ht.insert("kiwi", 60)
    print("After inserting 'kiwi':")
    print(ht)
if __name__ == "__main__":
    print("=== Testing Hash Table with Chaining ===")
    test_hash_table()