n = int(input())
count = {}
for i in range(n):
    word = input()
    if word in count:
        count[word] += 1
    else:
        count[word] = 1
    
print(len(count))
print(*count.values())