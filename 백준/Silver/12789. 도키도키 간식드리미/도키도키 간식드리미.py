# 12789
# Node 클래스
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Stack
class Stack:
    def __init__(self):
        self.top = None
    # push
    def push(self, data):
        if self.top == None:
            self.top = Node(data) # 비어 있다면 새로운 노드를 만들어서 가리키게 하자
        else:
            curr = Node(data)     # 비어있지 않다면 해당 data를 가진 Node를 만들고
            curr.next = self.top  # 만들어진 노드의 next에 원래 top을 가리키게!!
            self.top = curr       # top을 방금 만들어진 node를 가리키게!!
    # pop
    def pop(self):
        if self.top == None:
            return None
        else:
            curr = self.top
            self.top = self.top.next
            return curr.data
    # peek
    def peek(self):
        if self.top == None:
            return None
        else:
            curr = self.top
            return curr.data
    # is_empty
    def is_empty(self):
        return self.top == None

# 몇 명
N = int(input())
wait_list = list(map(int, input().split()))
s = Stack()

check = 1
is_nice = True

while len(wait_list) != 0:
    if check == wait_list[0]:
        del wait_list[0]
        check += 1
    else:
        while s.peek() == check:
            s.pop()
            check +=1

        s.push(wait_list[0])
        del wait_list[0]

while s.is_empty() == 0:
    if s.pop() == check:
        check += 1
    else:
        is_nice = False
        break

print("Nice" if is_nice else "Sad")