if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
        
    query_name = input()
    marks = student_marks[query_name]
    length = len(marks)
    total_marks = sum(marks)
    avg = total_marks / length
    print(f"{avg:.2f}")