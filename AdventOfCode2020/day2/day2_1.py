#!python3

from collections import Counter
from typing import List, Tuple


def read_file(file_name: str) -> List[Tuple]:
    passwords_policy_data: List[Tuple] = []
    with open(file_name) as file:
        for line in file:
            line.strip()
            policy_parsing = line.split(":")[0].split()
            password = line.split(":")[1].strip()
            letter = policy_parsing[1].strip()
            frequency_min = int(policy_parsing[0].split("-")[0])
            frequency_max = int(policy_parsing[0].split("-")[1])
            t: Tuple = (password, letter, frequency_min, frequency_max)
            passwords_policy_data.append(t)
    return passwords_policy_data


def get_valid_passwords_sum(passwords_policy_data: List[Tuple]) -> int:
    result: int = 0
    for password_data in passwords_policy_data:
        (password, letter, frequency_min, frequency_max) = password_data
        frequency_letter = Counter(password)[letter]
        if (frequency_max >= frequency_letter >= frequency_min):
            result += 1
    return result


def main():
    passwords_policy_data: List[Tuple] = read_file("AdventOfCode2020/day2/day2.txt")
    valid_passwords_sum: int = get_valid_passwords_sum(passwords_policy_data)
    print(f"The valid passwords sum is {valid_passwords_sum}")    


if __name__ == "__main__":
    main()