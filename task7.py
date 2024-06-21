if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    for student_name, marks_list in student_marks.items():
        if student_name == query_name:
            average_marks = sum(marks_list)/ len(marks_list)
            print(f"{average_marks:.2f}")