"""
Author: Miguel Da Silva
Description: Solution to Day 4 of the Advent of Code 2024 challenge.
"""

import numpy as np
from pathlib import Path

SCRIPT_DIR = Path(__file__).parent


def load_data(file_name):
    with open(SCRIPT_DIR / file_name) as f:
        lines = [list(line.strip()) for line in f if line.strip()]
    return np.array(lines)


def part1_solution(data_file_name):
    words_grid = load_data(data_file_name)
    nb_rows, nb_cols = words_grid.shape
    nb_xmas = 0

    # Searching horizontally
    for row in range(nb_rows):
        for col in range(nb_cols - 3):
            word = "".join(words_grid[row, col : col + 4])
            if word == "XMAS" or word == "SAMX":
                nb_xmas += 1

    # Searching vertically
    for row in range(nb_rows - 3):
        for col in range(nb_cols):
            word = "".join(words_grid[row : row + 4, col])
            if word == "XMAS" or word == "SAMX":
                nb_xmas += 1

    # Search diagonally
    for row in range(nb_rows - 3):
        for col in range(nb_cols - 3):
            word = ""
            for i in range(4):
                word = word + words_grid[row + i, col + i]
            if word == "XMAS" or word == "SAMX":
                nb_xmas += 1

    # Search along the inverted diagonals
    for row in range(nb_rows - 3):
        for col in range(3, nb_cols):
            word = ""
            for i in range(4):
                word = word + words_grid[row + i, col - i]
            if word == "XMAS" or word == "SAMX":
                nb_xmas += 1

    return nb_xmas


def part2_solution(data_file_name):
    words_grid = load_data(data_file_name)
    nb_rows, nb_cols = words_grid.shape
    nb_xmas = 0

    for row in range(nb_rows - 2):
        for col in range(nb_cols - 2):
            word_diag1 = ""
            word_diag2 = ""
            for i in range(3):
                word_diag1 = word_diag1 + words_grid[row + i, col + i]
                word_diag2 = word_diag2 + words_grid[row + i, col + 2 - i]
            if (word_diag1 == "MAS" or word_diag1 == "SAM") and (
                word_diag2 == "MAS" or word_diag2 == "SAM"
            ):
                nb_xmas += 1

    return nb_xmas


if __name__ == "__main__":
    print("Part 1 solution with test data:", part1_solution("day4_test_data.txt"))
    print("Part 1 solution with real data:", part1_solution("day4_data.txt"))
    print("---")
    print("Part 2 solution with test data:", part2_solution("day4_test_data.txt"))
    print("Part 2 solution with real data:", part2_solution("day4_data.txt"))
