import math
v1=int(input("Enter the Value"))
v2=int(input("Enter the Value"))
z1=int(input("Enter the Value"))
z2=int(input("Enter the Value"))
v3=v2-v1
z3=z2-z1
v4=math.pow(v3,2)
z4=math.pow(z3,2)
d=v4+z4
distance=math.sqrt(d)
print("Distance Between Two Points is",distance)
 

