import argparse
import math
h = float(input("Enter the height: "))
t = math.sqrt(2*h/9.8)
t = float("{0:.3f}".format(t))
print("Time taken is: ",t)


def Main():
     parser = argparse.ArgumentParser()
     parser.add_argument("num", help="The height of the ball you wish to calculate.", type=int)
     args = parser.parse_args()
     result = fib(args.num)
     print("The height of the ball is",h-s,"meters")

if __name__ == '__main__':
     Main()
