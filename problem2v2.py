import sys
import math

if len(sys.argv)>1:
     for arg in sys.argv[1:]:
          print(arg)
else:
     print('No arguments provided.')

def time(b, x):

    gamma = 1 / (math.sqrt(1 - b ** 2))
    x_contracted = x / gamma
    t_earth = x / b
    t_spaceship = x_contracted / b
    return t_earth, t_spaceship

b= float(.99)
x = float(arg)

t_earth, t_spaceship = time(b, x)
text = "time in earth's frame is {} year\
 and time in shaceship's frame is {} year".format(str(t_earth),str(t_spaceship))

print(text)
