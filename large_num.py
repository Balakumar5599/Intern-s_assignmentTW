inp_num=input("Enter the number")
list1=[]
for items in inp_num:
    list1.append((items))
list1.sort(reverse=True)
large_num=''
for x in list1:
    large_num=large_num+x
print(large_num)
#print(list1)
