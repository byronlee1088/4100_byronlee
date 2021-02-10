import argparse
import math

def fib(n):
     h=float(input("Enter the height: "))
     t=math.sqrt(2*h/9.8)
     t=float("{0:.3f}".format(t))
     return t

def Main():
     parser = argparse.ArgumentParser()
     parser.add_argument("num", help="The height of the ball you wish to calculate.", type=int)
     args = parser.parse_args()
     result = fib(args.num)
     print("The height of the ball is",fib(args.num),"meters")

if __name__ == '__main__':
     Main()
