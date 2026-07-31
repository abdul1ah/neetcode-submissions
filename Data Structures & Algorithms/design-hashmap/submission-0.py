class MyHashMap:

    def __init__(self):
        self.n = 1399
        self.lists = [[]for _ in range(self.n)]
        

    def put(self, key: int, value: int) -> None:
            index = key % self.n
            bucket = self.lists[index]

            for pair in bucket:
                if pair[0] == key:
                    pair[1] = value
                    return

            bucket.append([key, value])
        

    def get(self, key: int) -> int:
        index = key % self.n
        bucket = self.lists[index]

        for pairs in bucket:

            if pairs[0] == key:
                return pairs[1]

        return -1
               

    def remove(self, key: int) -> None:
        index = key % self.n
        bucket = self.lists[index]

        for pair in bucket:
            if pair[0] == key:
                bucket.remove(pair)


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)