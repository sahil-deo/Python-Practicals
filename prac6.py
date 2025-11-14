class HashTable:
    def __init__(self, size):
        self.hashTable = [None]*size
        self.size = size

    def hashFunction(self, key):
        return key%self.size

    def insert(self, key):
        index=self.hashFunction(key)
        start_index = index
        while self.hashTable[index]!=None and self.hashTable[index]!="DELETED":
            if self.hashTable[index]==key:
                print("Key Exists")
                return

            index=(index+1)%self.size
            if index==start_index:
                print("Table is full")

                return

        self.hashTable[index]=key
        print(f"{key} inserted at {index}")

    def delete(self, key):
        index = self.search(key)
        if self.hashTable[index]!=None:
            self.hashTable[index]="DELETED"
            print(f"{key} delete at {index}")
                    

    def search(self, key):
        index = self.hashFunction(key)
        start_index=key
        while self.hashTable[index]!=None:
            if self.hashTable[index]==key:
                print(f"{key} found at {index}")
                return index

            index=(index+1)%self.size
            if index == start_index:
                break

        print(f"{key} not found")



    def display(self):
        print(self.hashTable)



table = HashTable(10)

table.insert(5)
table.insert(10)
table.insert(15)
table.display()
table.search(5)
table.search(15)
table.delete(10)
table.display()
table.search(10)
    
                
