#Modified program

def function_outside():
    msg="Hi"
    def function_inside():
        nonlocal msg
        msg="Hello"
        print(msg)
    function_inside()
function_outside()
print(msg)

