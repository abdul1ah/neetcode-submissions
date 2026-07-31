class MyHashSet:

    def __init__(self):
        self.n = 1000 
        
        self.array = [[] for _ in range(self.n)]

    def add(self, key: int) -> None:
        index = key % self.n
        bucket = self.array[index]
        
        if key not in bucket:
            bucket.append(key)
        
    def remove(self, key: int) -> None:
        index = key % self.n
        bucket = self.array[index]
        
        if key in bucket:
            bucket.remove(key)

    def contains(self, key: int) -> bool:
        index = key % self.n 
        bucket = self.array[index]
        
        return key in bucket