#!python3

from typing import List
from fish import Fish

def read_file(file_name) -> List[Fish]:
    fish_school: List[Fish] = []
    with open(file_name) as f:
        for line in f:
            internal_timers = line.strip().split(",")
            for timer in internal_timers:
                fish: Fish = Fish(int(timer))
                fish_school.append(fish)
    return fish_school


def fish_school_timers(fish_school: List[Fish]) -> List[int]:
    timers: List[int] = []
    for fish in fish_school:
        timers.append(fish.get_timer())
    return timers


def fish_school_growth(fish_school: List[Fish], days: int) -> int:
    for day in range(days):
        new_fish_group: List[Fish] = []
        for i in range(len(fish_school)):
            timer: int = fish_school[i].get_timer()
            if timer == 0:
                new_fish: Fish = Fish(internal_timer = 8)
                new_fish_group.append(new_fish)
                fish_school[i].set_timer(internal_timer = 6)
            else:
                timer = timer - 1
                fish_school[i].set_timer(internal_timer = timer)
        fish_school.extend(new_fish_group)
    return len(fish_school)
    

def main():
    fish_school: List[Fish] = read_file("AdventOfCode2021/day6/day6_1.txt")
    fish_amount: int = fish_school_growth(fish_school, days = 80)
    print("\n\nHow many lanternfish would there be after 80 days?")
    print(f"fish amount: {fish_amount}")
    

if __name__ == "__main__":
    main()