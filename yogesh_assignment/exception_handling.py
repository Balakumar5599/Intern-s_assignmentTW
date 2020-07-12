#Exception handling program

def exception_func():
    
    try:
        num=int(input("Enter the interger: "))
        print("Sucessfully u entered an interger")
        
    except:
        print("Sorry, U have to enter the input again as an integer")
        exception_func()

exception_func()

    

