times = input()
num1, num2 = times.split()
num1 = int(num1)
num2 = int(num2)
num1_list = []
num2_list = []
for N1 in range(num1):
    insert = input()
    num1_list.append(insert)
for N2 in range(num2):
    insert = input()
    num2_list.append(insert)


for N2 in num2_list:
    position = []
    for i in range(len(num1_list)):
        if N2 == num1_list[i]:
          location = i
          location += 1
          position.append(location)
    if len(position) == 0:
       print(-1)
    else:
      print(*position)        

