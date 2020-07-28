class Vehicle:

    def __init__(self,name,km_range,price,ac_or_not,max_people):

        self.name=name
        self.km_range=km_range
        self.price=price
        self.ac_or_not=ac_or_not
        self.max_people=max_people

    
class GoRide:

    def __init__(self,category,ac_or_not):
        
        self.category=category
        self.ac_or_not=ac_or_not
        self.vehi_list=vehi_list
        
    def check_category_and_print_max_people(self):
        
        for vehicle in self.vehi_list:
            if vehicle.name==self.category and vehicle.ac_or_not==self.ac_or_not:
                print("\nNote: Maximum number of people allowed in "+self.category+":",vehicle.max_people)
                return True
        else:
            return False
        
    def display_price_menu(self,vehi_list):
        
        if self.check_category_and_print_max_people()==True:
            print("\n*******Menu for "+self.category+"*******\n")
            print("Category  Km range\tprice\n")
            for vehicle in self.vehi_list:
                if vehicle.name==self.category and vehicle.ac_or_not==self.ac_or_not:
                    print(vehicle.name,"\t",vehicle.km_range,"\tRs."+str(vehicle.price))

            if self.category=="auto" and self.ac_or_not=="yes":
                print("No Ac available for auto")

    def book_or_not(self,vehi_list):
        
        for vehicle in self.vehi_list:
            if (self.category==vehicle.name) and (self.ac_or_not==vehicle.ac_or_not):
                return "*****Your ride is booked*****"
        return "Please enter proper category or AC type"

        

category=input("Enter anyone of the category from[auto,micro,xl]: ").lower()
ac_or_not=input("\nDo you want AC [type:yes/no]: ").lower()

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

vehi_list=[auto1,auto2,auto3,micro1,micro2,micro3,micro4,xl1,xl2,xl3,xl4]

goride=GoRide(category,ac_or_not)
goride.display_price_menu(vehi_list)
print("\n",goride.book_or_not(vehi_list))

'''

output:-

Enter anyone of the category from[auto,micro,xl]: micro

Do you want AC [type:yes/no]: yes

Note: Maximum number of people allowed in micro: 4

*******Menu for micro*******

Category  Km range	price

micro 	 upto 15km 	Rs.12
micro 	 15 and above 	Rs.10

 *****Your ride is booked*****
 
 '''
