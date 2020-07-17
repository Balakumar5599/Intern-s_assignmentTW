class Product:
    
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
        
        
cream=Product(101,"Ice cream",300,"dairy")
pant=Product(102,"Pant",800,"textile")
tomato=Product(103,"Tomato",150,"produce")
table=Product(104,"Table",1400,"home needs")
chocolate=Product(105,"Chocolate",1500,"dairy")
potato=Product(106,"Potato",200,"produce")
shirt=Product(107,"Shirt",600,"textile")
chair=Product(108,"Chair",900,"home needs")
milk=Product(109,"Milk",100,"dairy")
saree=Product(110,"Saree",2000,"textile")

def total_tax():
    
    product_list=[cream,pant,tomato,table,chocolate,potato,shirt,chair,milk,saree]
    overall_bill=0
    overall_tax=0
    
    for prod in product_list:
        
        if prod.category=="textile":
            total_tax=Product.common_tax(prod)+prod.price*0.01
            print("Tax amount of "+prod.name+": Rs."+str(total_tax),"--->Total price of "+prod.name+": Rs.",prod.price+total_tax)
        elif prod.category=="dairy" and prod.price>1000:
            total_tax=Product.common_tax(prod)+prod.price*0.03
            print("Tax amount of "+prod.name+": Rs."+str(total_tax),"--->Total price of "+prod.name+": Rs.",prod.price+total_tax)
        else:
            total_tax=Product.common_tax(prod)
            print("Tax amount of "+prod.name+": Rs."+str(Product.common_tax(prod)),"--->Total price of "+prod.name+": Rs.",prod.price+total_tax)
            
        overall_bill+=prod.price+total_tax
        overall_tax+=total_tax
        
    print()    
    print("Overall Tax Amount: Rs.",overall_tax,"\n")
    print("Overall Bill Amount: Rs.",overall_bill)
    
total_tax()

'''
My output:-

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
