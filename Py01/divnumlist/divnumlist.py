#!python3
# script that prints first N numbers divisible by 3 or 5 
import argparse
parser = argparse.ArgumentParser(description="The script prints first N numbers divisible by 3 or 5")
parser.add_argument("N", type=int, help="integer to show the list of numbers divisible by 3 or 5 ")
parser.add_argument("-d", "--divisors", required=True, help="")
args = parser.parse_args()
N = args.N
div = args.divisors.split(",")

def toInteger(x: str) -> int:
    try:
        return int(x)
    except ValueError:
        print("Only integers, please")

def isInteger(x: str) -> bool:
    try:
        int(x)
        return True
    except ValueError:
        print("Only integers, please")

def unique(unique_list: list, item: int) -> list:
    if item not in unique_list:
        unique_list.append(item)
    return unique_list


is_int = False
unique_list = []
for x in div:
    is_int = isInteger(x)
    if not (is_int):
        break
    else:
        unique_list = unique(unique_list, toInteger(x))

#print(f" original list: {div}\n unique list: {unique_list}")

if (is_int == True):
    for x in range(1, N + 1):
        for i in unique_list:
            if (x % i == 0):
                print(x)
                break