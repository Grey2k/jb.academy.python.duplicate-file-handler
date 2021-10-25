from collections import deque

# put your python code here
test = input()

OPEN = '('
CLOSE = ')'

expression = deque()
error = False

for char in test:
    if char == OPEN:
        expression.append(OPEN)

    if char == CLOSE:
        if len(expression) == 0:
            error = True
            break
        if expression.pop() != OPEN:
            error = True
            break

if len(expression) != 0:
    error = True

print('OK' if not error else 'ERROR')
