class product:
    
    def __init__(self,pid,name,price,category):
        self.pid=pid
        self.name=name
        self.price=price
        self.category=category

    def common_tax(self):
        if self.price>=500:
            self.tax_price=self.price*0.05
        else:
            self.tax_price=self.price*0.02
        return self.tax_price
        
class TotalTax(product):

    def __init__(self,pid,name,price,category):
        product.__init__(self,pid,name,price,category)

    def total_tax(self):
        if self.category=="textile":
            self.total_tax=product.common_tax(self)+self.price*0.01
        elif self.category=="dairy" and self.price>1000:
            self.total_tax=product.common_tax(self)+self.price*0.03
        else:
            self.total_tax=product.common_tax(self)
        return self.total_tax

cream=TotalTax(101,"Ice cream",300,"dairy")
pant=TotalTax(102,"Pant",800,"textile")
tomato=TotalTax(103,"Tomato",150,"produce")
table=TotalTax(104,"Table",1400,"home needs")
chocolate=TotalTax(105,"Chocolate",1500,"dairy")
potato=TotalTax(106,"Potato",200,"produce")
shirt=TotalTax(107,"Shirt",600,"textile")
chair=TotalTax(108,"Chair",900,"home needs")
milk=TotalTax(109,"Milk",100,"dairy")
saree=TotalTax(110,"Saree",2000,"textile")

def overall_func():
    overall_tax=0
    overall_bill=0
    for prod in product_list:
        print("Tax amount of "+prod.name+": Rs."+str(TotalTax.total_tax(prod)),"--->Total price of "+prod.name+": Rs.",prod.price+TotalTax.total_tax(prod))
        overall_tax+=TotalTax.total_tax(prod)
        overall_bill+=prod.price+TotalTax.total_tax(prod)
    print()
    print("Overall Tax Amount: Rs.",overall_tax)
    print("Overall Bill Amount: Rs.",overall_bill,"\n")
    
    
product_list=[cream,pant,tomato,table,chocolate,potato,shirt,chair,milk,saree]
overall_func()

'''
My Output

Tax amount of Ice cream: Rs.6.0 --->Total price of Ice cream: Rs. 306.0
Tax amount of Pant: Rs.48.0 --->Total price of Pant: Rs. 848.0
Tax amount of Tomato: Rs.3.0 --->Total price of Tomato: Rs. 153.0
Tax amount of Table: Rs.70.0 --->Total price of Table: Rs. 1470.0
Tax amount of Chocolate: Rs.120.0 --->Total price of Chocolate: Rs. 1620.0
Tax amount of Potato: Rs.4.0 --->Total price of Potato: Rs. 204.0
Tax amount of Shirt: Rs.36.0 --->Total price of Shirt: Rs. 636.0
Tax amount of Chair: Rs.45.0 --->Total price of Chair: Rs. 945.0
Tax amount of Milk: Rs.2.0 --->Total price of Milk: Rs. 102.0
Tax amount of Saree: Rs.120.0 --->Total price of Saree: Rs. 2120.0

Overall Tax Amount: Rs. 454.0
Overall Bill Amount: Rs. 8404.0
'''
