from typing import List

class HashSet:

    def __init__(self):
        self.h = {}

    def add(self, key: int) -> None:
        self.h[key] = 0

    def remove(self, key: int) -> None:
        if self.h.get(key) is not None:
            self.h.pop(key)

    def contains(self, key: int) -> bool:
        if self.h.get(key) == 0:
            return True
        else:
            return False

# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)

#我的解法
class MyHashSet:

    def __init__(self):
        self.set = [-1 for _ in range(1000001)]  
    def get_key(self,key: int ) -> int :

        return key%1000001
    def add(self, key: int) -> None:
        i=self.get_key(key)
        self.set[i]=key

    def remove(self, key: int) -> None:
        i=self.get_key(key)
        self.set[i]=-1

    def contains(self, key: int) -> bool:
        i=self.get_key(key)
        if self.set[i] == -1 :
            return False
        else :
            return True
obj = MyHashSet()
obj.add(1)
obj.add(2)
#obj.remove(key)
param_3 = obj.contains(1)
print(param_3)