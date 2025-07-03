people = []
marks = []

def calculate_grade(average):
    if average >= 70:
        return 'A'
    elif average >= 60:
        return 'B'
    elif average >= 50:
        return 'C'
    else:
        return 'D'


Tlofstudents = int(input("Enter the number of students: "))
tlofmarks = int(input("Enter the number of tests: "))


for i in range(Tlofstudents):
    name = input("Enter student name: ")
    score_list = []

    for j in range(tlofmarks):
        score = float(input(f"Enter score for paper {j+1}: "))
        score_list.append(score)

    avg_score = sum(score_list) / tlofmarks
    grade = calculate_grade(avg_score)

    people.append(name)
    marks.append([score_list, avg_score, grade])

print("\n--- Student Results ---")
for i in range(Tlofstudents):
  for j in range(tlofmarks):
    print(f"{people[i]} - Scores: {marks[i][j]}, Avg: {marks[i][j]}, Grade: {marks[i][j]}")
