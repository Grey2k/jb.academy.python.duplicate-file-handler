from collections import deque

# please don't change the following line
candy_bag = deque(input().split())

COMMAND_PUSH = 'PUT'
COMMAND_POP = 'TAKE'

# your code here
n = int(input().strip())

for _ in range(n):
    input_cmd = input().split()

    cmd = input_cmd[0]

    if cmd == COMMAND_POP:
        if candy_bag:
            print(candy_bag.pop())
        else:
            print('We are out of candies :(')

    if cmd == COMMAND_PUSH:
        value = input_cmd[1]
        candy_bag.append(value)
