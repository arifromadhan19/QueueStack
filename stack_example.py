class Stack:
    def __init__(self):
        self.items = []

    # Memeriksa apakah stack kosong
    def isEmpty(self):
        return self.items == []

    # Menambah objek/data ke dalam stack
    def push(self, item):
        self.items.append(item)

    # Mengeluarkan data dari stack
    def pop(self):
        return self.items.pop()

    # Menampilkan objek terakhir dari stack
    def peek(self):
        # return self.items[-1]
        return self.items[len(self.items)-1]

    # Mehitung panjang stack
    def size(self):
        return len(self.items)

s = Stack()
s.push(54)
s.push(45)
s.push("+")

print(s.size())
print(s.pop())
# while not s.isEmpty():
#     print(s.pop(), end=" ")
print(s.peek())

# m = Stack()
# m.push('x')
# m.push('y')
# m.pop()
# m.push('z')
# print(m.peek())


