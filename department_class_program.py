#Department program:-

class Department:

    def __init__(self,dept_name,dept_students,dept_subjects):
        self.dept_name=dept_name
        self.dept_students=dept_students
        self.dept_subjects=dept_subjects

    def display(self):
        print("\nNames of the students in",self.dept_name,"department: ")
        for student in range(len(self.dept_students)):
            print(self.dept_students[student])

class Student:

    def __init__(self,dept_name,iD,stud_name,stud_sub):

        self.dept_name=dept_name
        self.iD=iD
        self.stud_name=stud_name
        self.stud_sub=stud_sub


ece_dept=Department("ECE",["Bala","Barath","Dhanesh","Gogul","Mani"],["EC1","ED","M1","Physics","Chemistry"])
mech_dept=Department("Mechanical",["Balaji","Dinesh","Maari","poo","Sivaguru"],["M1","Physics","Mechanics","CAT","Chemistry"])
biomed_dept=Department("Biomedical",["Ajith","Ranjan","Santhosh","Surya","Varatharajan"],["Bio tech","Physics","Chemistry","Medical","Cardio"])

stud1=Student("ECE",1,"Bala",["ED","M1","Physics","EC1"])
stud2=Student("Mechanical",5,"Poo",["Physics","M1","Mechanics"])
stud3=Student("Biomedical",3,"Surya",["Bio tech","Chemistry","Medical","Cardio"])
stud4=Student("ECE",8,"Dhanesh",["ED","Physics","M1"])

def overlap():

    overlap_sub = set.intersection(set(ece_dept.dept_subjects),set(mech_dept.dept_subjects),set(biomed_dept.dept_subjects))
    print("Subjects that are overlap btw various departments:\n",list(overlap_sub))

overlap()
ece_dept.display()       #Just change the obj name here, for which department student names you want.

stud_list=[stud1,stud2,stud3,stud4]
print("\nName of the departments, where students take more than 3 courses: ")
for stud in stud_list:
    if len(stud.stud_sub)>3:
        print(stud.dept_name)

