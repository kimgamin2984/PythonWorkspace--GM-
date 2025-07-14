import sys

n = int(sys.stdin.readline())
stack = []
for i in range(n):
    command = sys.stdin.readline().split()
    if command[0] == 'push':
        stack.append(int(command[1]))
    if command[0] == 'pop':
        if len(stack) == 0:
            sys.stdout.write('-1\n')
        else:
            sys.stdout.write(f'{stack.pop()}\n')
    if command[0] == 'size':
        sys.stdout.write(f'{len(stack)}\n')
    if command[0] == 'empty':
        if len(stack) == 0:
            sys.stdout.write('1\n')
        else:
            sys.stdout.write('0\n')
    if command[0] == 'top':
        if len(stack) == 0:
            sys.stdout.write('-1\n')
        else:
            sys.stdout.write(f'{stack[-1]}\n')