name = input("Enter your Name: ")
roll = input("Enter your roll Number : ")

num = int(input("Enter Number of Subjects: "))
subject=[]
marks=[]


for i in range (num):
    sub = input("Entre subject name:")
    mar = int(input("Entre marks :"))
    subject.append(sub)
    marks.append(mar)

total = sum(marks)
average = total / num

if min(marks) < 35:
     result="fail"
     print("\nMotivation: Don’t give up! ")

else:
    result="pass"
print("\nMotivation: Great job! ")
if average >= 90 and average <=100:
    grade ="A"
elif average >= 75 and average <=89:
  grade ="B"
elif average >= 60 and average <=74:
  grade = "c"
elif average>=35 and Average<=49:
    grade="D"
elif average<=34:
    print(f"you are Failed{average}")
else:
     grade ="f"

bestscore = marks.index(max(marks))
weakscore=marks.index(min(marks))

print("\n---------------------------")
print("***STUDENT PROGRESS REPORT***")
print("-----------------------------")
print(f"Student name  : {name}")
print(f"Roll number.  : {roll}")
print("----------------------------")
print(f"Student and marks:")
for s, m in zip(subject, marks):
    print(f"{s:<12}.  :  {m}")
print(f"Totalmarks.    : {total}")
print(f"Average       :  {round(average, 2)}")
print(f"Grade.        :  {grade}")
print(f"Result        : {result}")
print(f"Best Score    :  {subject[bestscore]} ({marks[bestscore]})")
print(f"Weak Score    :  {subject[weakscore]} ({marks[weakscore]})")
print("\n---------------------------")
while True:
    print("\nWhat do you want to do next?")
    print("1. Enter marks again")
    print("2. View report again")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        print("You chose to enter marks again...\n")
        break

    elif choice == "2":
        print("Showing the report again...\n")
        generate_report(name, roll, subjects, marks)

    elif choice == "3":
        print("Thank you! Exiting the program...")
        exit()

    else:
        print("Invalid choice! Please select 1, 2, or 3.")
