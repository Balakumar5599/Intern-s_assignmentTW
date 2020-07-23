
class IceCream:

    def __init__(self,types,flavours,toppings):
        self.types=types
        self.flavours=flavours
        self.toppings=toppings

    def type_cost(self):
        cost=self.types[icecream[0]]
        return cost

    def flavour_cost(self):
        cost=self.flavours[icecream[1]]
        return cost

    def topping_cost(self):
        cost=0
        if "chocolate" in icecream and opt=="yes":
            cost+=self.toppings[topp_inp]
        return cost

class Stall:

    def __init__(self):
        self.ice_obj=IceCream(types,flavours,toppings)

    def icecream_total_cost(self):
        self.ice_cost=self.ice_obj.type_cost()+self.ice_obj.flavour_cost()+self.ice_obj.topping_cost()
        return self.ice_cost

    def create_icecream_list(self):
        self.icecream_list=[]
        for typ,typ_cost in types.items():
            for flav,flav_cost in flavours.items():
                self.icecream_list.append(typ+" "+flav+" "+str(typ_cost+flav_cost))
        return self.icecream_list

class MenuCard:

    def __init__(self):
        self.ice_list=Stall()

    def show_menu_card(self):
        print("\n**********Menu Card**********")
        print("\nTYPE\t FLAVOUR\t COST\n")
        for ice in self.ice_list.create_icecream_list():
            print(ice.split()[0],"\t",ice.split()[1],"\t","RS."+ice.split()[2])
        print()
        
types={"stick":20,"cone":30,"cup":40}
flavours={"chocolate":40,"vanilla":35,"strawberry":45}
toppings={"chocochips":15,"caramel":20,"nuts":25}

stall=Stall()
menu=MenuCard()
menu.show_menu_card()

#main body
icecream=input("Enter the icecream u want: ").lower().split()
quantity=int(input("Enter the quantity u want: "))
if "chocolate" in icecream:
    print("\nAdditional topping options\n")
    for name,cost in toppings.items():
        print(name,": Rs.",cost)
        print()
    opt=input("Do u want toppings [yes/no]: ").lower()
    if opt=="yes":
        topp_inp=input("\nEnter anyone in the toppin option: ").lower()
        try:
            print("\nTotal price for your order is: Rs."+str(quantity*stall.icecream_total_cost()))
        except:
            print("-------Please enter the proper topping in the option-------")
    else:
        print("\nTotal price for your order is: Rs."+str(quantity*stall.icecream_total_cost()))
else:
    print("\nTotal price for your order is: Rs."+str(quantity*stall.icecream_total_cost()))

