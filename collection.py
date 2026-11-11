from collections import deque
n = int(input())
container = deque([])
for i in range(n):
    insert = input().split()
    if insert[0] == "append":
        amount = insert[1]
        container.append(amount)
    elif insert[0] == "appendleft":
        amount = insert[1]
        container.appendleft(amount)
    elif insert[0] == "pop":
        container.pop()
    elif insert[0] == "popleft":
        container.popleft()

print(*container)
        