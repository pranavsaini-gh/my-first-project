class ArrayDatabase:
    def __init__(self, capacity):
        self.arr = [None] * capacity
        self.size = 0

    def insert(self, index, value):
        if index < 0 or index > self.size or self.size == len(self.arr):
            return
        for i in range(self.size, index, -1):
            self.arr[i] = self.arr[i - 1]
        self.arr[index] = value
        self.size += 1

    def delete(self, index):
        if index < 0 or index >= self.size:
            return
        for i in range(index, self.size - 1):
            self.arr[i] = self.arr[i + 1]
        self.arr[self.size - 1] = None
        self.size -= 1

    def search(self, value):
        for i in range(self.size):
            if self.arr[i] == value:
                return i
        return -1

    def display(self):
        print([self.arr[i] for i in range(self.size)])


db = ArrayDatabase(10)
db.insert(0, 5)
db.insert(1, 10)
db.insert(2, 15)
db.display()

db.delete(1)
db.display()

print("Found at index:", db.search(15))
