class HashTable:
    data = []
    size = 0

    def __init__(self, size: int):
        self.data = [[]] * size
        self.size = size

    def _hash(self, key: str) -> int:
        i_hash = 0
        for ch in key:
            i_hash = (i_hash + ord(ch)) % self.size

        return i_hash

    # Time Complexity: O(1) in the average case
    # Time Complexity [worst-case]: O(n)
    def get(self, key: str) -> int or str or None:
        mem_pos = self._hash(key)

        if self.data[mem_pos]:
            if len(self.data[mem_pos]) > 1:
                for i in range(len(self.data[mem_pos])):
                    if self.data[mem_pos][i][0] == key:
                        return self.data[mem_pos][i]

                else:
                    return ['NULL', 0]

            else:
                return self.data[mem_pos] if self.data[mem_pos][0][0] == key else ['NULL', 'NULL']

        else:
            return ['NULL', 'NULL']

    # Time Complexity: O(1) in the average case
    # Time Complexity [worst-case]: O(n)
    def set(self, key: str, value: int or str or None):
        if key and value:
            mem_pos = self._hash(key)

            if not self.data[mem_pos]:
                self.data[mem_pos] = [[key, value]]

            else:
                self.data[mem_pos].extend([[key, value]])

        else:
            print("Please provide both key and value pair")


myHashTable = HashTable(100)
myHashTable.set('grapes', 100)
myHashTable.set('anime', 1000)
myHashTable.set('animation', 990)
myHashTable.set('the_code_ninja', 16)
myHashTable.set('manga', 220)
myHashTable.set('tokyo_revengers', 580)
myHashTable.set('naruto', 500)
myHashTable.set(key='ninja', value='Can code or something')

input_key = str(input('key: '))
print(f"the key '{input_key}' is at {myHashTable.get(input_key)}")
print(myHashTable.data)
