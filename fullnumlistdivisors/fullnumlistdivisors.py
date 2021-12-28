#!python3
# script that prints first N numbers divisible by --divisors=3,5,77,...
import argparse
from typing import List, Dict, Set
#from sortedcontainers import SortedSet

parser = argparse.ArgumentParser(description="The script prints first N numbers divisible by 3 or 5")
parser.add_argument("-n", required=True, type=int, help="integer to show the list of numbers divisible by 3 or 5 ")
parser.add_argument("-d", "--divisors", required=True, help="")
args = parser.parse_args()

def unique_divisors_set(unique_set: Set[int], dividor: int) -> Set[int]:
    unique_set.add(dividor)
    return unique_set


def main():
    error_check_pass = False
    unique_set: Set[int] = set()
    divisors = args.divisors.split(",")
    for divisor in divisors:
        try:
            unique_set = unique_divisors_set(unique_set, int(divisor))
            error_check_pass = True
        except ValueError:
            print("Only integers, please")
            error_check_pass = False
            break

    if (error_check_pass == True):
        sorted_unique_divisors: List[int] = sorted(unique_set)
        numbers_set: Set[int] = set()
        for divisor_index in range(len(sorted_unique_divisors)):
            divisor = sorted_unique_divisors[divisor_index]
            for i in range(1, args.n + 1):
                numbers_set.add(divisor * i)
        firsN_numbers = sorted(numbers_set)[0:args.n]    
        print(f"First {args.n} number(s) divisible by divisors: {sorted_unique_divisors} \n{firsN_numbers}")
     
    
if __name__ == "__main__":
    main()