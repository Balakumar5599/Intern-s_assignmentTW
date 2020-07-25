class CarDetail:
    
    def __init__(self,category,number,colour,company,model):
        self.category=category
        self.number=number
        self.colour=colour
        self.company=company
        self.model=model

    def get_car_detail(self):
        self.car_details="Car category is "+self.category+", Number is "+self.number+",colour is "+self.colour+", Company is "+self.company+" and model is "+self.model
        return self.car_details
    

class DriverDetail:
    
    def __init__(self,name,age,lic_num,valid_date):
        self.name=name
        self.age=age
        self.lic_num=lic_num
        self.valid_date=valid_date

    def get_driver_detail(self):
        self.driver_detail="Driver name is "+self.name+", Age is "+str(self.age)+",license number is "+self.lic_num+" and validity period is "+self.valid_date
        return self.driver_detail

class GoRide:
    
    max_micro=4
    max_xl=10

    def __init__(self):
        
        self.car_obj=car_obj
        self.driver_obj=driver_obj
        
    def registration(self):
        register_list=[]
        register_list.append(self.car_obj.get_car_detail())
        register_list.append(self.driver_obj.get_driver_detail())
        return register_list
    
    def display_registration_status(self):
        if len(driver_name)>0:
            print("Congratulation!!!You are successfully registered in GoRide")
        else:
            print("You are not sucessfully registered in GoRide")
            
print("\n*************************Welcome To GoRide*************************")
print("-Micro includes all cars that can accommodate a maximum upto 4 people")
print("-XL includes all cars that can accommodate a maximum upto 10 people")
        
car_category=input("\nEnter the category of the car: ")
car_num=input("Enter the car number: ")
car_colour=input("Enter the car colour: ")
car_company=input("Enter the car company name: ")
model=input("Enter the car model: ")
car_obj=CarDetail(car_category,car_num,car_colour,car_company,model)

driver_name=input("\nEnter the driver name: ")
driver_age=int(input("Enter the driver age: "))
driver_license_num=input("Enter the driver license number: ")
driver_license_validity=input("Enter the driver license validity time: ")
driver_obj=DriverDetail(driver_name,driver_age,driver_license_num,driver_license_validity)
goride=GoRide()

print()

for details in goride.registration():
    print(details,"\n")
goride.display_registration_status()

'''
output:-

*************************Welcome To GoRide*************************
-Micro includes all cars that can accommodate a maximum upto 4 people
-XL includes all cars that can accommodate a maximum upto 10 people

Enter the category of the car: micro
Enter the car number: TN 06 AN 9315
Enter the car colour: yellow
Enter the car company name: BMW
Enter the car model: A5

Enter the driver name: Bala
Enter the driver age: 23
Enter the driver license number: MH134564566556778
Enter the driver license validity time: 06-07-2022

Car category is micro, Number is TN 06 AN 9315,colour is yellow, Company is BMW and model is A5 

Driver name is Bala, Age is 23,license number is MH134564566556778 and validity period is 06-07-2022 

Congratulation!!!You are successfully registered in GoRide
'''
