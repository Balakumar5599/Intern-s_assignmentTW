#Debugged program

'''
def f(x):
    def g(y):
        return y
    return g(y)
a=5
b=1
h=f(a)
h(b)
'''

#Modified program

def f(x):
    def g(y):
        return y
    return g
a=5
b=1
h=f(a)
print(h(b))

'''Explanation:-


        In modified program,the function f(x) return the inner function reference.
Thus,h=f(a) is used to assign the g(inner func reference) to h and now it is act like function
So it accept argument and thus we can call and print the called output using print.



        In debugged program,the function f(x) return the g(y) function.thus
h=f(a),its is used to store the returned value of f(x) which is nothing but inner function
so we cannot call it and also we are able to assign value for y.thus it shows error.
        
'''
