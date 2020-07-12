# Check odd or even using list comprehension

rang=int(input("Enter the range: "))
num_list=[2,1,32,7,4,5,8,7,10,34]
check_list=["Even" if num_list[i]%2==0 else "Odd" for i in range(rang)]
print(check_list)
