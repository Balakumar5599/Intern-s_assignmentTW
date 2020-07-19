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
                
def topping():
    
    toppings={"chocochips":15,"caramel":20,"nuts":25}
    print("\nAdditional topping options for chocolate icecream:-\n")
    for name,cost in toppings.items():
        print(name,":",cost)
              
    def chocolate():
              
        option=input("\nDo u want any topping for ur chocolate icecream ?Type(Yes/No): ").lower()
        if option=="yes":
            topp_inp=input("\nEnter anyone of the topping options: ").lower().replace(" ","")
            if topp_inp in toppings.keys():
                try:
                    print("\nTotal cost of "+ice_input+" is:",quantity*(ice_dict[ref_inp]+toppings[topp_inp]))
                except:
                    print("\nPlease enter the icecream only in the Menu card")
            else:
                print("\n-----Please enter the proper topping option-----")
                chocolate()
        else:
            print("\nTotal cost for "+ice_input+" is:",quantity*(ice_dict[ref_inp]))
    chocolate()

icecream=IceCream({"stick":20,"cone":30,"cup":40},{"chocolate":40,"vanilla":35,"strawberry":45})
icecream.menu_card()

ice_input=input("\nEnter the Ice cream do you want: ")
ref_inp=ice_input.lower().replace(" ","").replace("icecreams","").replace("ice","").replace("cream","")
quantity=int(input("Enter the quantity of Ice cream: "))


        
if "chocolate" in ref_inp:
    topping()
elif "chocolate" not in ref_inp:
    try:
        print("\nTotal cost for "+ice_input+" is:",quantity*(ice_dict[ref_inp]))
    except:
        print("\nPlease enter the icecream in the Menu card")
else:
    print("\nPlease enter proper input")
    
