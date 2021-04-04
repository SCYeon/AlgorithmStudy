import sys

n = int(sys.stdin.readline())

queue = []

for i in range(n):
    value = sys.stdin.readline().split()

    if value[0] == "push":
        queue.insert(0,value[1])
    elif value[0] == "pop":
        if len(queue) != 0: print(queue.pop())
        else: print(-1)
    elif value[0] == "size":
        print(len(queue))
    elif value[0] == "empty":
        if len(queue) == 0: print(1)
        else: print(0)
    elif value[0] == "front":
        if len(queue) == 0: print(-1)
        else: print(queue[len(queue)-1])
    elif value[0] == "back":
        if len(queue) == 0: print(-1)
        else: print(queue[0])

