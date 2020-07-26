class Vehicle:

    def __init__(self,km,ac_or_nac):
        self.km=km
        self.ac_or_nac=ac_or_nac

class Auto(Vehicle):

    max_people_auto=3
    
    def __init__(self,km,ac_or_nac):
        Vehicle.__init__(self,km,ac_or_nac)
        
    def get_auto_price(self):

        if self.km<=15:
            return 10
        
        elif 15<self.km<30:
            return 8
        
        elif self.km>=30:
            return 15

        elif self.ac_or_nac=="no":
            return 0

class Micro(Vehicle):

    max_people_micro=4

    def __init__(self,km,ac_or_nac):
        Vehicle.__init__(self,km,ac_or_nac)


    def get_micro_price(self):

        if self.km<15 and self.ac_or_nac=="yes":
            return 12
        
        if self.km<15 and self.ac_or_nac=="no":
            return 14
        
        if self.km>=15 and self.ac_or_nac=="yes":
            return 10
        
        if self.km>=15 and self.ac_or_nac=="no":
            return 12

class Xl(Vehicle):

    max_people_xl=10

    def __init__(self,km,ac_or_nac):
        Vehicle.__init__(self,km,ac_or_nac)


    def get_xl_price(self):

        if self.km<15 and self.ac_or_nac=="yes":
            return 14
        
        if self.km<15 and self.ac_or_nac=="no":
            return 15
        
        if self.km>=15 and self.ac_or_nac=="yes":
            return 14
        
        if self.km>=15 and self.ac_or_nac=="no":
            return 15

class GoRide:

    def __init__(self,category,type_acnac):
        
        self.category=category
        self.type_acnac=type_acnac


    def display_goride(self):
        
        if self.category=="auto" and self.type_acnac=="no":
            print("\n*******Menu For Auto*******\nkm range\tprice with AC\n")
            print("Upto 15km-\tRs.10/km\n15-30km-\tRs.8/km\n30km and above-\tRs.15/km\n")
        elif self.category=="auto" and self.type_acnac=="yes":
            print("\nNo Ac available for Auto\n")
        elif self.category=="micro" and self.type_acnac=="yes":
            print("\n*******Menu For Micro*******\nkm range\tprice with AC\n")
            print("Upto 15km-\tRs.12/km\n15km and above-\tRs.10/km\n")
        elif self.category=="micro" and self.type_acnac=="no":
            print("\n*******Menu For Micro*******\nkm range\tprice with NAC\n")
            print("Upto 15km-\tRs.14/km\n15km and above-\tRs.12/km\n")
        elif self.category=="xl" and self.type_acnac=="yes":
            print("\n*******Menu For Xl*******\nkm range\tprice with AC\n")
            print("Upto 15km-\tRs.14/km\n15km and above-\tRs.14/km\n")
        elif self.category=="xl" and self.type_acnac=="no":
            print("\n*******Menu For Xl*******\nkm range\tprice with NAC\n")
            print("Upto 15km-\tRs.15/km\n15km and above-\tRs.15/km\n")
            

    def total_cost(self):
        
        if category=="auto" and ac_or_not=="no":
            print("\nNote: Maximum number of people allowed:",auto.max_people_auto)
            print("\nTotal cost for ur booking is:",km*auto.get_auto_price())
        elif category=="micro":
            print("\nNote: Maximum number of people allowed:",micro.max_people_micro)
            print("\nTotal cost for ur booking is:",km*micro.get_micro_price())
        elif category=="xl":
            print("\nNote: Maximum number of people allowed:",xl.max_people_xl)
            print("\nTotal cost for ur booking is:",km*xl.get_xl_price())
        


category=input("Enter anyone of the category from[auto,micro,xl]: ").lower()
ac_or_not=input("Do you want AC [type:yes/no]: ").lower()
go=GoRide(category,ac_or_not)
go.display_goride()

km=int(input("Enter the kilometers u want to go: "))
auto=Auto(km,ac_or_not)
micro=Micro(km,ac_or_not)
xl=Xl(km,ac_or_not)
go.total_cost()

'''
Enter anyone of the category from[auto,micro,xl]: micro
Do you want AC [type:yes/no]: yes

*******Menu For Micro*******
km range	price with AC

Upto 15km-	Rs.12/km
15km and above-	Rs.10/km

Enter the kilometers u want to go: 40

Note: Maximum number of people allowed: 4

Total cost for ur booking is: 400
'''
