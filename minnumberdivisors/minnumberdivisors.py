#!python3
# script that prints first N numbers divisible by --divisors=3,5,77,...
import argparse
from typing import List, Dict, Set

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
        divisible_numbers_set: Set[int] = set()
        unique_divisors_list: List[int] = list(unique_set)
        temporary_divisors_list: List[int] = list(unique_set)
        
        while (len(divisible_numbers_set) < args.n):
            min_number = min(temporary_divisors_list)
            divisible_numbers_set.add(min_number)
            index = temporary_divisors_list.index(min_number)
            temporary_divisors_list[index] += unique_divisors_list[index]
        
        print(f"Divisors list: {unique_divisors_list}")
        print(f"First {args.n} numbers divisible by those divisors: {sorted(divisible_numbers_set)}")
        
    
if __name__ == "__main__":
    main()