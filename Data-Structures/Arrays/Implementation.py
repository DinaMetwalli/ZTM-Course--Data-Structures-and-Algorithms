# Implementation of Array data structure.

class MyArray():
    def __init__(self):
        self.length = 0
        self.data = {}

    def get_array(self) -> int | object:
        print(f"length: {self.length}, items: {self.data}")
        return self.length, self.data
    
    def get_item(self, index) -> object:
        return self.data[index]
    
    def push(self, item) -> int:
        self.data[self.length] = item
        self.length+=1
        return self.length
    
    def pop(self):
        last_item = self.data[self.length-1]
        del self.data[self.length-1]
        self.length-=1
        return last_item
    
    def delete(self, index):
        item = self.data[index]
        self.shift_items(index)
        self.length-=1
        return item

    def shift_items(self, index) -> None:
        for i in range(index, self.length-1):
            self.data[i] = self.data[i+1]
        del self.data[self.length-1]
        return
    

arr = MyArray()
# print(arr)

print(arr.push(15))
print(arr.push('you'))
print(arr.push('are'))
print(arr.push(4.22))
arr.get_array()
print(arr.pop())
print(arr.delete(0))
print(arr.push('nice'))
print(arr.push('!'))
arr.get_array()
