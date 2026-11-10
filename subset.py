test = int(input())
for i in range(test):
    set_A = ()
    set_B = ()
    n1 = int(input())
    set_A = set(map(int, input().split()))
    n2 = int(input())
    set_B = set(map(int, input().split()))
    print(set_A.issubset(set_B))
    
