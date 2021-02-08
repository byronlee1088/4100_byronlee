import math

def time(beta, x):

    gamma = 1 / (math.sqrt(1 - beta ** 2))
    x_contracted = x / gamma

    t_earth = x / beta
    t_spaceship = x_contracted / beta

    return t_earth, t_spaceship

beta= float(input("Enter the velocity as multiple of speed of light\t"))
x = float(input("Enter the distance in light year\t"))

t_earth, t_spaceship = time(beta, x)
text = "time in earth's frame is {} year\
and time in shaceship's frame is {} year".format(str(t_earth),str(t_spaceship))

print(text)
