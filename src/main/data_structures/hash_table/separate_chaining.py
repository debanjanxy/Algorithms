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
        if bucket:
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
            if self.size > self.threshold:
                self.resize_table()
            return None
        else:
            old_index, old_entry = old_entry
            self.table[bucket_index][old_index] = new_entry
            return old_entry

    def resize_table(self):
        self.capacity *= 2
        self.threshold = int(self.capacity * self.max_load_factor)
        new_table = [None] * self.capacity
        for i, entries in enumerate(self.table):
            if entries:
                for j, entry in enumerate(entries):
                    bucket_index = self.normalize_index(entry.hash)
                    if not new_table[bucket_index]:
                        new_table[bucket_index] = []
                    new_table[bucket_index].append(entry)
                self.table[i].clear()
        self.table = new_table

    def get(self, key):
        bucket_index = self.normalize_index(hash(key))
        entry_result = self.bucket_seek_entry(bucket_index, key)
        if not entry_result:
            raise KeyError(f"{key} is not present")
        else:
            _, entry = entry_result
        return entry.value

    def remove(self, key):
        bucket_index = self.normalize_index(hash(key))
        return self.bucket_remove_entry(bucket_index, key)

    def bucket_remove_entry(self, bucket_index, key):
        entry_result = self.bucket_seek_entry(bucket_index, key)
        if not entry_result:
            raise KeyError(f"{key} is not present in the table")
        else:
            entry_index, entry = entry_result
            self.table[bucket_index].remove(entry)
            self.size -= 1
            return entry.value
        

if __name__ =="__main__":
    ht = HashTableSeparateChaining()
    ht.add("deb", 11)
    ht.add("titi", 9)
    ht.add("mamta", 11)
    ht.add("aapt", 43)
    ht.add("abc", 23)
    ht.add("rty", 12)
    print(ht.contains_key("deb"))
    print(ht.contains_key("hello"))
    print(ht.get("titi"))
    print(ht.contains_key("abc"))
    print(ht.remove("abc"))
    print(ht.contains_key("abc"))