#File handling

file=open("my_file.txt","w")
file.write("My name is Balakumar M \nMy DOB is 05/05/1999\n")
file.close()
file=open("my_file.txt","a")
file.write("My Degree is BE,ECE")
file.close()
file=open("my_file.txt","r")
print(file.readline())
print(file.readline())
print(file.readline())
file.close()

#My output is look like
'''
My name is Balakumar M 

My DOB is 05/05/1999

My Degree is BE,ECE
'''
