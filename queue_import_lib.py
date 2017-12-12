import queue

Fq = queue.Queue()

for i in range(5):
    Fq.put(i)

while not Fq.empty():
    print(Fq.get(), end=' ')

print("\n")
Lq = queue.LifoQueue()

for i in range(5):
    Lq.put(i)

while not Lq.empty():
    print(Lq.get(), end=' ')
