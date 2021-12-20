#!python3
# print integer numbers from N to M (accept --n and --m) 

import argparse
parser = argparse.ArgumentParser(description="The script prints integer numbers from N to M (accept --n and --m)")
parser.add_argument("-n", "--n", type=int, required=True, help="integer numbers")
parser.add_argument("-m", "--m", type=int, required=True, help="integer numbers")
args = parser.parse_args()

def enterNumbersError():
    print("\nTo show the list of numbers from N to M enter two integer numbers where N < M\n")

arg1 = args.n
arg2 = args.m
if (arg1 > arg2):
    enterNumbersError()
else:
    for i in range(arg1, arg2 + 1):
        print(i)
