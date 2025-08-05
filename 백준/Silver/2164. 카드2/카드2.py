# 2164
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, data):
        if self.front == None:
            curr = Node(data)
            self.front = curr
            self.rear = curr
        else:
            curr = Node(data)
            self.rear.next = curr
            self.rear = curr

    def dequeue(self):
        if self.front == None:
            return None
        else:
            curr = self.front
            self.front = self.front.next
            return curr.data

    def is_empty(self):
        return self.front == None

N = int(input())

q = Queue()

for i in range(1, N + 1):
    q.enqueue(i)

while q.front != q.rear:
    q.dequeue()
    q.enqueue(q.dequeue())

print(q.dequeue())