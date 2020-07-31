class Vehicle:

    def __init__(self,name,km_range,price,ac_service,max_people):

        self.name=name
        self.km_range=km_range
        self.price=price
        self.ac_service=ac_service
        self.max_people=max_people

    
class GoRide:

    def __init__(self,category,ac_service):
        
        self.category=category
        self.ac_service=ac_service
        self.vehicle_list=vehicle_list
        
    def check_category_and_ac_service(self,vehicle_list):
        
        for vehicle in self.vehicle_list:
            if vehicle.name==self.category and vehicle.ac_service==self.ac_service:
                print("\nNote: Maximum number of people allowed in "+self.category+":",vehicle.max_people)
                return True
        else:
            return False
        
    def display_price_menu(self,vehicle_list):
        
        if self.check_category_and_ac_service(vehicle_list)==True:
            print("\n*******Menu for "+self.category+"*******\n")
            print("Category  Km range\tprice\n")
            for vehicle in self.vehicle_list:
                if vehicle.name==self.category and vehicle.ac_service==self.ac_service:
                    print(vehicle.name,"\t",vehicle.km_range,"\tRs."+str(vehicle.price))

        if self.category=="auto" and self.ac_service=="yes":
            print("No Ac available for auto")

    def do_u_want_to_book(self,vehicle_list):
        
        if goride.check_category_and_ac_service(vehicle_list)==False:
            print("Please enter proper category or Ac service")
        else:
            confirmation=input("\nDo you want to book ride?: ")
            if confirmation=="yes":
                print("\n*****Sucessfully booked in GoRide*****")
            elif confirmation=="no":
                print("\nYou are not booked in GoRide")

        

category=input("Enter anyone of the category from[auto,micro,xl]: ").lower()
ac_service=input("\nDo you want AC [type:yes/no]: ").lower()

auto1=Vehicle("auto","upto 15km",10,"no",3)
auto2=Vehicle("auto","15-30km",8,"no",3)
auto3=Vehicle("auto","30 and above",15,"no",3)
micro1=Vehicle("micro","upto 15km",12,"yes",4)
micro2=Vehicle("micro","upto 15km",14,"no",4)
micro3=Vehicle("micro","15 and above",10,"yes",4)
micro4=Vehicle("micro","15 and above",12,"no",4)
xl1=Vehicle("xl","upto 15km",14,"yes",10)
xl2=Vehicle("xl","upto 15km",15,"no",10)
xl3=Vehicle("xl","15 and above",14,"yes",10)
xl4=Vehicle("xl","15 and above",15,"no",10)

vehicle_list=[auto1,auto2,auto3,micro1,micro2,micro3,micro4,xl1,xl2,xl3,xl4]

goride=GoRide(category,ac_service)
goride.display_price_menu(vehicle_list)
goride.do_u_want_to_book(vehicle_list)

'''

output:-

Enter anyone of the category from[auto,micro,xl]: micro

Do you want AC [type:yes/no]: yes

Note: Maximum number of people allowed in micro: 4

*******Menu for micro*******

Category  Km range	price

micro 	 upto 15km 	Rs.12
micro 	 15 and above 	Rs.10

 *****Sucessfully booked in GoRide*****
 
 '''
