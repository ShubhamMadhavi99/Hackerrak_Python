def avg(lst):
    return (lst[0]+lst[1]+lst[2])/3

n = int(input())
student_marks = {}
for _ in range(n):
    name, *line = input().split()
    scores = list(map(float, line))
    student_marks[name] = scores
query_name = input()

print(f'{avg(student_marks[query_name]):.2f}')