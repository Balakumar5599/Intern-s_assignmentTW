class IceCream:
    
    def __init__(self,types,flavours):
        self.types=types
        self.flavours=flavours
        
    def menu_card(self):

        print("*****Menu Card*****\n")
        global ice_dict
        ice_dict={}
        for typ,typ_cost in self.types.items():
            for flav,flav_cost in self.flavours.items():
                ice_dict[typ+flav]=typ_cost+flav_cost
                print(typ,flav,"Icecream:",typ_cost+flav_cost)

class ChocolateIce(IceCream):
    
    def __init__(self,types,flavours,toppings):
        IceCream.__init__(self,types,flavours)
        self.toppings=toppings
        
    def topping(self):
        print("\nAdditional topping options for chocolate icecream:-\n")
        for name,cost in self.toppings.items():
            print(name,":",cost)
        

icecream=ChocolateIce({"stick":20,"cone":30,"cup":40},{"chocolate":40,"vanilla":35,"strawberry":45},{"chocochips":15,"caramel":20,"nuts":25})
icecream.menu_card()

ice_input=input("\nEnter the Ice cream do you want: ")
ref_inp=ice_input.lower().replace(" ","").replace("icecreams","").replace("ice","").replace("cream","")
quantity=int(input("Enter the quantity of Ice cream: "))

def chocolate():
    icecream.topping()
    option=input("\nDo u want any topping for ur chocolate icecream ?Type(Yes/No): ").lower()
    if option=="yes":
        topp_inp=input("\nEnter anyone of the topping options: ").lower().replace(" ","")
        if topp_inp in icecream.toppings.keys():
            print("\nTotal cost of "+ice_input+" is:",quantity*(ice_dict[ref_inp]+icecream.toppings[topp_inp]))
        else:
            print("\n-----Please enter the proper topping option-----")
            chocolate()
    else:
        print("\nTotal cost for "+ice_input+" is:",quantity*(ice_dict[ref_inp]))
        
if "chocolate" in ref_inp:
    chocolate()
elif "chocolate" not in ref_inp:
    print("\nTotal cost for "+ice_input+" is:",quantity*(ice_dict[ref_inp]))
else:
    print("\nPlease enter proper input")
    
