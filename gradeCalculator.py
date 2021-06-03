#student_scores is a dictionary
student_scores = {"Aditya":'99',"Aastha":'78',"Arunima":'81',"Neha":'74',"Pankuri":'62'}
#now create an empty dictionary
students_grade={}
#this will copy the student_scores dictionary into the students_grade dictionary
students_grade = student_scores.copy()
print("printing students scores => ")
print(student_scores)
for key in student_scores:
    scores = int(student_scores[key])
    if scores >= 91 and scores <=100:
        students_grade[key] = "Outstanding"
    if scores >=81 and scores <91:
        students_grade[key]="exceeded expectations"
    if scores >=71 and scores <81:
        students_grade[key]="acceptable"
    if scores <71:
        students_grade[key]="failed"
print("printing students grade =>")
print(students_grade)