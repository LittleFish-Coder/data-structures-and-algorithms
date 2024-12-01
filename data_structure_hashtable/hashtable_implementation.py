class Hashtable:
    def __init__(self):
        self.bucket = 16
        self.hashmap = [[] for _ in range(self.bucket)]

    def __str__(self):
        return str(self.__dict__)
    
    def hash(self, key):
        return len(key) % self.bucket
    
    def put(self, key, value):
        hash_value = self.hash(key)
        reference = self.hashmap[hash_value]
        for i in range(len(reference)):
            if reference[i][0] == key:
                reference[i][1] = value
                return value
        reference.append([key, value])
        return None
    
    def get(self, key):
        hash_value = self.hash(key)
        reference = self.hashmap[hash_value]
        for i in range(len(reference)):
            if reference[i][0] == key:
                return reference[i][1]
        return -1

    def remove(self, key):
        hash_value = self.hash(key)
        reference = self.hashmap[hash_value]
        for i in range(len(reference)):
            if reference[i][0] == key:
                reference.pop(i)
                return None
        return None

hashtable = Hashtable()
hashtable.put('grapes',1000)
hashtable.put('apples',10)
hashtable.put('ora',300)
hashtable.put('banan',200)
print(hashtable.get('grapes'))
print(hashtable)
hashtable.remove('apples')
print(hashtable)