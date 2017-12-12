class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueueLIFO(self, item):
        self.items.insert(0,item)

    def enqueueFIFO(self, item):
        self.items.append(item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

    def peek(self):
        return self.items[len(self.items) - 1]

q=Queue()
q.enqueueLIFO(4)
q.enqueueLIFO('dog')
q.enqueueLIFO(True)
print(q.size())
# print(q.isEmpty())
# q.enqueue(8.4)
# print(q.dequeue())
# print(q.dequeue())
# print(q.size())
# print(q.peek())
for n in q.items:
    print ("This time, it's: "+ str(n))

