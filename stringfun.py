def string_test(s):
    if len(s) > 2 and (s[0] == s[-1]):
        return(True)
    else:
        return(False)

def add_x(s):
    return("x" + s + "x")
    

    
y= "test"
x = string_test(y)
print(x)
z= add_x(y)
print(z)

    
