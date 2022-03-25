#!python3

from typing import List, Tuple


def read_file(file_name) -> List[Tuple]:
    passwords_policy_data: List[Tuple] = []
    with open(file_name) as file:
        for line in file:
            line.strip()
            policy_parsing = line.split(":")[0].split()
            password = line.split(":")[1].strip()
            letter = policy_parsing[1].strip()
            position_first = int(policy_parsing[0].split("-")[0])
            position_second = int(policy_parsing[0].split("-")[1])
            t: Tuple = (password, letter, position_first, position_second)
            passwords_policy_data.append(t)
    return passwords_policy_data


def get_valid_passwords_sum(passwords_policy_data: List[Tuple]) -> int:
    result: int = 0
    for pass_data in passwords_policy_data:
        (password, letter, position_first, position_second) = pass_data
        matches: int = 0
        if password[position_first - 1] == letter: matches += 1
        if password[position_second - 1] == letter: matches += 1
        if matches == 1: result += 1
        
        #print(f"{password}  letter={letter} ({position_first}, {position_second})   matches = {matches}")
    return result



def main():
    passwords_policy_data: List[Tuple] = read_file("AdventOfCode2020/day2/day2.txt")
    valid_passwords_sum: int = get_valid_passwords_sum(passwords_policy_data)
    print(f"The valid passwords sum is {valid_passwords_sum}")  


if __name__ == "__main__":
    main()