N = int(input())
numbers = list(map(int, input().split()))
result = []
checks = []
for num in numbers:
    checks.append(num > 0)
result.append(all(checks))
checks2 = []
for num in numbers:
    new_num = str(num)
    checks2.append(new_num == new_num[::-1])
result.append(any(checks2))
print(all(result))