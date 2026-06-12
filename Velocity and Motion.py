s=float(input("Initial drop height? "))
v=float(input("Initial velocity? "))
h=float(input("Ending height? "))

print("")
print("Answer:")

t=((-v)+(((v*v)-(4*-16*(s-h)))**0.5))/-32 # Quadratic Formula (based on vertical motion formula)
if t>0:
    print(str(t) + " seconds")
else: # If original t is the negative root
    t=((-v)-(((v*v)-(4*-16*(s-h))))**0.5)/-32
    print(str(t) + " seconds")