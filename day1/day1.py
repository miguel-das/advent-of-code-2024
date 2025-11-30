"""
Author: Miguel Da Silva
Description: Solution to Day 1 of the Advent of Code 2024 challenge.
"""

import numpy as np
from pathlib import Path

SCRIPT_DIR = Path(__file__).parent

def load_data(file_name):
    """Load data from a text file into a NumPy array."""
    data = np.genfromtxt(SCRIPT_DIR / file_name)
    return data


# Part 1
def part1_solution(data_file_name):
    """
    Returns the solution of the part1 of the day1 challenge as an integer
    """
    my_array = load_data(data_file_name)

    # Sort both lists
    my_arrayA = np.sort(my_array[:, 0])
    my_arrayB = np.sort(my_array[:, 1])

    # Compute the absolute distances
    dist_AB = np.abs(my_arrayB - my_arrayA)

    return int(np.sum(dist_AB))


# Part 2
def part2_solution(data_file_name):
    """
    Returns the solution of the part2 the day1 challenge as an integer
    """
    my_array = load_data(data_file_name)

    # Split into two separate lists
    my_arrayA = my_array[:, 0]
    my_arrayB = my_array[:, 1]

    # Initialize the similarity vector
    similarity_array = np.zeros(len(my_arrayA))

    # Compute the similarity scores
    for i in range(len(my_arrayA)):
        similarity_array[i] = list(my_arrayB).count(my_arrayA[i]) * my_arrayA[i]

    return int(np.sum(similarity_array))


if __name__ == "__main__":
    print("Part 1 test:", part1_solution("day1_test_data.txt"))
    print("Part 1 solution:", part1_solution("day1_data.txt"))
    print("---")
    print("Part 2 test:", part2_solution("day1_test_data.txt"))
    print("Part 2 solution:", part2_solution("day1_data.txt"))
