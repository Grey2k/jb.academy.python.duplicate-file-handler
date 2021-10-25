from collections import deque

COMMAND_PUSH = 'PUSH'
COMMAND_POP = 'POP'

n = int(input().strip())

stack = deque()

for _ in range(n):
    input_cmd = input().split()

    cmd = input_cmd[0]

    if cmd == COMMAND_POP:
        stack.pop()

    if cmd == COMMAND_PUSH:
        value = input_cmd[1]
        stack.append(value)

while len(stack) > 0:
    print(stack.pop())
