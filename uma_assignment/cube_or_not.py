#Given number is cube or not

num=int(input("Enter the input: "))
result=round(num**(1/3))**3==num
cube_or_not=lambda result:"True" if result==True else "False"
print(cube_or_not(result))
