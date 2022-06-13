import math

class Entry:
    def __init__(self, k, v):
        self.key = k
        self.value = v
        self.hash = hash(k)

    def equals(self, other):
        if self.hash != other.hash:
            return False
        return self.key == other.key

    def to_string(self):
        return f"{self.key} => {self.value}"


class HashTableSeparateChaining:
    def __init__(self, capacity=3, max_load_factor=0.75):
        if capacity < 0:
            raise ValueError("Illegal capacity")
        if max_load_factor < 0 or math.isinf(max_load_factor):
            raise ValueError("Illegal Load Factor")
        self.capacity = max(capacity, 3)
        self.size = 0
        self.max_load_factor = max_load_factor
        self.threshold = int(self.capacity * max_load_factor)
        self.table = [None] * self.capacity
        
    def size(self):
        return self.size

    def is_empty(self):
        return self.size() == 0

    def normalize_index(self, key_hash):
        return (key_hash & 0x7FFFFFFF) % self.capacity

    def clear(self):
        self.table.clear()
        self.size = 0

    def contains_key(self, k):
        bucket_index = self.normalize_index(hash(k))
        return self.bucket_seek_entry(bucket_index, k) != None

    def bucket_seek_entry(self, bucket_index, key):
        if not key:
            return None
        bucket = self.table[bucket_index]
        for i, elem in enumerate(bucket):
            if elem.key.__eq__(key):
                return (i, elem)
        return None

    def add(self, key, value):
        return self.insert(key, value)

    def put(self, key, value):
        return self.insert(key, value)

    def insert(self, key, value):
        if not key:
            raise ValueError("Illegal key")
        new_entry = Entry(key, value)
        bucket_index = self.normalize_index(new_entry.hash)
        self.bucket_insert_entry(bucket_index, new_entry)

    def bucket_insert_entry(self, bucket_index, new_entry):
        bucket = self.table[bucket_index]
        if not bucket:
            self.table[bucket_index] = bucket = []
        old_entry = self.bucket_seek_entry(bucket_index, new_entry.key)
        if not old_entry:
            self.table[bucket_index].append(new_entry)
            self.size += 1
            if self.size > self.capacity:
                self.resize_table()
            return None
        else:
            old_index, old_entry = old_entry
            self.table[bucket_index][old_index] = new_entry
            return old_entry

    def resize_table(self):
        pass


    

if __name__ =="__main__":
    ht = HashTableSeparateChaining()
    ht.add("deb", 11)
    ht.add("titi", 9)
    print(ht.contains_key("deb"))


    

