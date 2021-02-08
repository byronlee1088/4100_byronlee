import math

h = float(input("Enter the height: "))

t = math.sqrt(2*h/9.8)

t = float("{0:.3f}".format(t))

print("Time taken is: ",t)
