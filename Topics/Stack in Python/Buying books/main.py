from collections import deque

COMMAND_BUY = 'BUY'
COMMAND_READ = 'READ'

n = int(input().strip())
shelf = deque()
reads = deque()

for _ in range(n):
    input_cmd = input().split()

    command = input_cmd[0]
    book = input_cmd[1:]

    if command == COMMAND_BUY:
        shelf.append(" ".join(book))

    if command == COMMAND_READ:
        reads.append(shelf.pop())

while len(reads) > 0:
    print(reads.popleft())
