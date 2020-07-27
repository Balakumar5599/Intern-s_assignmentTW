class Vehicle:

    def __init__(self,name,km_range,price,ac_or_not):

        self.name=name
        self.km_range=km_range
        self.price=price
        self.ac_or_not=ac_or_not

    def display_price(self,vehi_list):
        print("\n*******Menu for "+category+"*******\n")
        print("Category  Km range\tprice\n")
        for vehicle in vehi_list:
            if vehicle.name==category and vehicle.ac_or_not==ac_or_not:
                print(vehicle.name,"\t",vehicle.km_range,"\tRs."+str(vehicle.price))

        if category=="auto" and ac_or_not=="yes":
            print("No Ac available for auto")
class GoRide:

    def __init__(self,category,ac_or_not):
        self.category=category
        self.ac_or_not=ac_or_not

    def book_or_not(self):
        for vehicle in vehi_list:
            if (self.category==vehicle.name) and (self.ac_or_not=="yes"or"no"):
                return "*****Your ride is booked*****"
        return "Please enter proper category"

        

category=input("Enter anyone of the category from[auto,micro,xl]: ").lower()
ac_or_not=input("\nDo you want AC [type:yes/no]: ").lower()

auto1=Vehicle("auto","upto 15km",10,"no")
auto2=Vehicle("auto","15-30km",8,"no")
auto3=Vehicle("auto","30 and above",15,"no")
micro1=Vehicle("micro","upto 15km",12,"yes")
micro2=Vehicle("micro","upto 15km",14,"no")
micro3=Vehicle("micro","15 and above",10,"yes")
micro4=Vehicle("micro","15 and above",12,"no")
xl1=Vehicle("xl","upto 15km",14,"yes")
xl2=Vehicle("xl","upto 15km",15,"no")
xl3=Vehicle("xl","15 and above",14,"yes")
xl4=Vehicle("xl","15 and above",15,"no")

vehi_list=[auto1,auto2,auto3,micro1,micro2,micro3,micro4,xl1,xl2,xl3,xl4]

vehicle_obj=Vehicle(category,"km range","price",ac_or_not)

vehicle_obj.display_price(vehi_list)

goride=GoRide(category,ac_or_not)
print("\n",goride.book_or_not())

'''

output:-

Enter anyone of the category from[auto,micro,xl]: micro

Do you want AC [type:yes/no]: yes

*******Menu for micro*******

Category  Km range	price

micro 	 upto 15km 	Rs.12
micro 	 15 and above 	Rs.10

 *****Your ride is booked*****
 '''
