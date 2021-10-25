from collections import deque

n = int(input())

stack = deque()
for _ in range(n):
    stack.append(input())

for _ in range(n):
    print(stack.pop())
