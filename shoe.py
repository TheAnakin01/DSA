from collections import Counter
N = int(input())
size = list(map(int, input().split()))
dict_size = Counter(size)
customers = int(input())
earnings = 0
for customer in range(customers):
    insert = list(map(int, input().split()))
    if insert[0] in dict_size and int(dict_size[insert[0]]) > 0:
        dict_size[insert[0]] -= 1
        earnings += insert[1]
    else:
        pass
print(earnings)
