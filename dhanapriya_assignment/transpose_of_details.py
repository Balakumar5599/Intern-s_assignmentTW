# Transpose of the students Detail:-


students=[['Priya','Mukii','Dhana','Mani'],['CSE','Civil','ECE','IT'],[1999,1998,2000,1997]]

transpose_list=[[inner_list[i] for inner_list in students] for i in range(len(students[1]))]

print(transpose_list)

