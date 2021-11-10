# Write your code here :-)
student = []
previous = 0

print("Please enter the total number of students available: ")
total_students = int(input())
print("Enter marks obtained by the " + str(total_students) + " students")

for n in range(total_students):
    student.append(int(input()))


for n in range(total_students):
    avg = previous + student[n]
    previous = avg

avg_class_score = avg / len(student)
print("Average Score ", avg_class_score)

avg_point_below = avg_class_score - 5
print("Average score below 5: ", avg_point_below)
counter = 1

for n in range(len(student)):
#     if int(student[n]) >= 60 and int(student[n]) > avg_point_below:
    if student[n] >= 60 and student[n] > avg_point_below:
        print(f"Student {counter} passed")
    elif student[n] < 60 or student[n] < avg_point_below:
        print(f"Student {counter} failed")
    else:
        print("Invalid input")
    counter += 1
