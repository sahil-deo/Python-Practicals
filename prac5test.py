class HashTable:
    def __init__(self, size):
        self.size=size
        self.table=[[]for _ in range (size)]

    def hashFunction(self, key):
        return key%self.size

    def insert(self, key, value):
        index = self.hashFunction(key)
        self.table[index].append((key,value))


    def search(self, key):
        index = self.hashFunction(key)
        for i in self.table[index]:
            if i[0] == key:
                return i[1]

        return None


    def delete(self, key):
        index = self.hashFunction(key)
        for i in range (len(self.table[index])):
            if self.table[index][i][0]==key:
                del self.table[index][i]
                return True

        return False

    def display(self):
        print(self.table)

    # start execution

hashTable = HashTable(5)
hashTable.insert(1, "A")
hashTable.display()
hashTable.insert(2, "B")
hashTable.display()
hashTable.delete(1)
hashTable.display()
print(hashTable.search(2))
print(hashTable.search(1))
  
