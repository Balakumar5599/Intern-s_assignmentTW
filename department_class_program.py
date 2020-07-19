#Department program:-

class Department:

    def __init__(self,dept_name,dept_students,dept_subjects):
        self.dept_name=dept_name
        self.dept_students=dept_students
        self.dept_subjects=dept_subjects

    def display(self):
        print("Names of the students in",self.dept_name,"department: ")
        for student in range(len(self.dept_students)):
            print(self.dept_students[student])

class Dept1(Department):

    def __init__(self,name,students,subjects):
        super().__init__(name,students,subjects)

class Dept2(Department):

    def __init__(self,name,students,subjects):
        super().__init__(name,students,subjects)

class Dept3(Department):

    def __init__(self,name,students,subjects):
        super().__init__(name,students,subjects)

class Student:

    def __init__(self,dept_name,iD,stud_name,stud_sub):

        self.dept_name=dept_name
        self.iD=iD
        self.stud_name=stud_name
        self.stud_sub=stud_sub


dept1=Dept1("ECE",["Bala","Barath","Dhanesh","Gogul","Mani"],["EC1","ED","M1","Physics","Chemistry"])
dept2=Dept2("Mechanical",["Balaji","Dinesh","Maari","poo","Sivaguru"],["M1","Physics","Mechanics","CAT","Chemistry"])
dept3=Dept3("Biomedical",["Ajith","Ranjan","Santhosh","Surya","Varatharajan"],["Bio tech","Physics","Chemistry","Medical","Cardio"])

stud1=Student("ECE",1,"bala",["ed","m1","phy","ec1"])
stud2=Student("Mechanical",1,"poo",["phy","m1","mechanics"])
stud3=Student("Biomedical",1,"surya",["bio","che","med","cario"])
stud4=Student("ECE",1,"dhanesh",["ed","phy","m1"])

def overlap():

    overlap_sub=(set(dept1.dept_subjects).intersection(set(dept2.dept_subjects).intersection(dept3.dept_subjects)))
    print("Subjects that are overlap btw various departments:\n",list(overlap_sub))

overlap()
dept1.display()

stud_list=[stud1,stud2,stud3,stud4]
print("Name of the departments, where students take more than 3 courses: ")
for stud in stud_list:
    if len(stud.stud_sub)>3:
        print(stud.dept_name)

