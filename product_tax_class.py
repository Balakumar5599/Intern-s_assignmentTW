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
        
        
def total_tax():
    
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
    print("Overall Bill Amount: Rs.(Incl.of all taxes)",overall_bill)

print("Note:\nThe category of products can be only one of these following: Dairy, Textile, Produce, Homeneeds\n")
num_of_product=int(input("Enter the number of products: "))
product_list=[]
for items_no in range(num_of_product):
    print()
    print("Enter the details of product",items_no+1,":-")
    pid=int(input("Enter the product ID: "))
    name=input("Enter the product name: ")
    obj_name=name.lower().replace(" ","")
    price=float(input("Enter the product price: "))
    category=input("Enter the product category: ").lower()
    obj_name=Product(pid,name,price,category)
    product_list.append(obj_name)
print()

total_tax()

'''
My output:-

Note:
The category of products can be only one of these following: Dairy, Textile, Produce, Homeneeds

Enter the number of products: 10

Enter the details of product 1 :-
Enter the product ID: 101
Enter the product name: icecream
Enter the product price: 300
Enter the product category: dairy

Enter the details of product 2 :-
Enter the product ID: 102
Enter the product name: pant
Enter the product price: 800
Enter the product category: textile

Enter the details of product 3 :-
Enter the product ID: 103
Enter the product name: tomato
Enter the product price: 150
Enter the product category: produce

Enter the details of product 4 :-
Enter the product ID: 104
Enter the product name: table
Enter the product price: 1400
Enter the product category: home needs

Enter the details of product 5 :-
Enter the product ID: 105
Enter the product name: chocolate
Enter the product price: 1500
Enter the product category: dairy

Enter the details of product 6 :-
Enter the product ID: 106
Enter the product name: potato
Enter the product price: 200
Enter the product category: produce

Enter the details of product 7 :-
Enter the product ID: 107
Enter the product name: shirt
Enter the product price: 600
Enter the product category: textile

Enter the details of product 8 :-
Enter the product ID: 108
Enter the product name: chair
Enter the product price: 900
Enter the product category: home needs

Enter the details of product 9 :-
Enter the product ID: 109
Enter the product name: milk
Enter the product price: 100
Enter the product category: dairy

Enter the details of product 10 :-
Enter the product ID: 110
Enter the product name: saree
Enter the product price: 2000
Enter the product category: textile

Tax amount of icecream: Rs.6.0 --->Total price of icecream: Rs. 306.0
Tax amount of pant: Rs.48.0 --->Total price of pant: Rs. 848.0
Tax amount of tomato: Rs.3.0 --->Total price of tomato: Rs. 153.0
Tax amount of table: Rs.70.0 --->Total price of table: Rs. 1470.0
Tax amount of chocolate: Rs.120.0 --->Total price of chocolate: Rs. 1620.0
Tax amount of potato: Rs.4.0 --->Total price of potato: Rs. 204.0
Tax amount of shirt: Rs.36.0 --->Total price of shirt: Rs. 636.0
Tax amount of chair: Rs.45.0 --->Total price of chair: Rs. 945.0
Tax amount of milk: Rs.2.0 --->Total price of milk: Rs. 102.0
Tax amount of saree: Rs.120.0 --->Total price of saree: Rs. 2120.0

Overall Tax Amount: Rs. 454.0 

Overall Bill Amount: Rs.(Incl.of all taxes) 8404.0
'''
