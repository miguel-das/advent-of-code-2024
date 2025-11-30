"""
Author: Miguel Da Silva
Description: Solution to Day 3 of the Advent of Code 2024 challenge.
"""

import re
from pathlib import Path

SCRIPT_DIR = Path(__file__).parent


def load_data(file_name):
    with open(SCRIPT_DIR / file_name) as f:
        corrupted_memory = f.read()
    return corrupted_memory


def part1_solution(data_file_name):
    corrupted_memory = load_data(data_file_name)
    pattern = r"mul\((\d{1,3}),(\d{1,3})\)"

    matches = re.findall(pattern, corrupted_memory)

    result = 0
    for x, y in matches:
        result += int(x) * int(y)

    return result


def part2_solution(data_file_name):
    corrupted_memory = load_data(data_file_name)
    pattern = r"do\(\)|don't\(\)|mul\((\d{1,3}),(\d{1,3})\)"

    matches = re.finditer(pattern, corrupted_memory)

    enabled = True
    result = 0

    for match in matches:
        if match.group() == "do()":  # group() = group(0) by default
            enabled = True
        elif match.group() == "don't()":
            enabled = False
        else:  # match.group() = mul(x,y)
            if enabled == True:
                x = match.group(1)
                y = match.group(2)
                result += int(x) * int(y)

    return result


if __name__ == "__main__":
    print("Part 1 solution with test data:", part1_solution("day3_test_data1.txt"))
    print("Part 1 solution with real data:", part1_solution("day3_data.txt"))
    print("---")
    print("Part 2 solution with test data:", part2_solution("day3_test_data2.txt"))
    print("Part 2 solution with real data:", part2_solution("day3_data.txt"))
