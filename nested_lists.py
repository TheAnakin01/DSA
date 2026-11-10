records = []
if __name__ == '__main__':
    for _ in range(int(input())):
        name = input()
        score = float(input())
        records.append([name, score])
    list1 = []
    for record in records:
        list1.append(record[1])
    sorted_list = sorted(set(list1))
    second_lowest = sorted_list[1]
    final_list = []
    for score in records:
        if score[1] == second_lowest:
         final_list.append(score)
    last_list = sorted(final_list)
    for name in last_list:
       print(name[0])
    

