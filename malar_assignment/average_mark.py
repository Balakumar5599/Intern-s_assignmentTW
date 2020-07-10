#method-1

def average_mark(name,marks):
    avg=sum(marks)/len(marks)
    print(name+'-',end="")
    print(avg)
name=input("Enter the name: ")
marks=list(map(int,input("Enter the marks: ").split(",")))
average_mark(name,marks)


#method-2:

def avg_mark(name,m1,m2,m3,m4,m5):
    avg=(m1+m2+m3+m4+m5)/5
    print(name+'-',end="")
    print(avg)
avg_mark("Bala",80,96,84,70,56)
