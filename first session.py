import pandas as pd
import matplotlib.pyplot as plt


data = {
    "student_id": [101, 102, 103, 104, 105, 106],
    "attendance_percent": [92, 67, 81, 45, 74, 88],
    "assignment_score": [18, 12, 15, 8, 14, 19],
    "quiz_score": [72, 48, 65, 30, 55, 80],
    "lab_completed": [True, False, True, False, True, True]
}

df = pd.DataFrame(data)


df['total_score'] = df['assignment_score'] + df['quiz_score']

df['eligible'] = (
    (df['attendance_percent'] >= 75) &
    (df['total_score'] >= 70) &
    (df['lab_completed'])
)


plt.figure(figsize=(6,4))
plt.bar(df['student_id'], df['attendance_percent'])
plt.title("Attendance Percentage")
plt.xlabel("Student ID")
plt.ylabel("Attendance (%)")
plt.show()


plt.figure(figsize=(6,4))
plt.bar(df['student_id'], df['total_score'])
plt.title("Total Score of Students")
plt.xlabel("Student ID")
plt.ylabel("Total Score")
plt.show()


plt.figure(figsize=(6,4))
plt.scatter(df['assignment_score'], df['quiz_score'])
plt.title("Assignment vs Quiz Score")
plt.xlabel("Assignment Score")
plt.ylabel("Quiz Score")

for i in range(len(df)):
    plt.text(df['assignment_score'][i],
             df['quiz_score'][i],
             str(df['student_id'][i]))

plt.show()


eligible_count = df['eligible'].value_counts()

plt.figure(figsize=(5,4))
plt.pie(eligible_count,
        labels=['Eligible', 'Not Eligible'],
        autopct='%1.1f%%')
plt.title("Eligibility Distribution")
plt.show()
