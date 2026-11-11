Test = int(input())
for i in range(Test):
    try:
        numbers = list(map(int, input().split()))
        num1 = numbers[0]
        num2 = numbers[1]
        print(int(num1 // num2))
    except ZeroDivisionError as e:
        print("Error Code:", e)
    except ValueError as e:
        print("Error Code:", e)