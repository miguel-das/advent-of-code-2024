"""
Author: Miguel Da Silva
Description: Solution to Day 2 of the Advent of Code 2024 challenge.
"""

import numpy as np
from pathlib import Path

SCRIPT_DIR = Path(__file__).parent

def load_data(file_name):
    """Load data into a list of lists"""
    with open(SCRIPT_DIR / file_name) as f:
        return [list(map(int, line.split())) for line in f if line.strip()]


def safety_test(report):
    """
    Returns the safety status of a given report
    1 = safe, 0 = unsafe
    """
    report_safety = 1
    # Compute adjacent differences
    diffs = np.zeros(len(report) - 1)
    for i in range(len(report) - 1):
        diffs[i] = report[i + 1] - report[i]

        # diff in [1,3]
        if abs(diffs[i]) < 1 or abs(diffs[i]) > 3:
            report_safety = 0

    # report numbers are only increasing or only decreasing
    if not (np.all(diffs > 0) or np.all(diffs < 0)):
        report_safety = 0

    return report_safety


# Part 1
def part1_solution(data_file_name):
    reports = load_data(data_file_name)
    reports_safety = np.ones(len(reports))
    # Checks the safety for all the reports using the "safety_test" function
    for report_idx in range(len(reports)):
        report = reports[report_idx]
        reports_safety[report_idx] = safety_test(report)

    return int(np.sum(reports_safety))  # Safety score


def part2_solution(data_file_name):
    reports = load_data(data_file_name)
    reports_safety = np.ones(len(reports))
    for report_idx in range(len(reports)):
        report = reports[report_idx]
        reports_safety[report_idx] = safety_test(report)

        # If a report is not safe, we try to make it safe using the problem dampner
        # eg. we check if removing one element from the report makes it safe or not
        if reports_safety[report_idx] == 0:
            for j in range(len(report)):
                modified_report = report.copy()
                modified_report.pop(j)
                reports_safety[report_idx] = safety_test(modified_report)
                if reports_safety[report_idx] == 1:
                    break

    return int(np.sum(reports_safety))


if __name__ == "__main__":
    print("Part 1 solution with test data:", part1_solution("day2_test_data.txt"))
    print("Part 1 solution with real data:", part1_solution("day2_data.txt"))
    print("---")
    print("Part 2 solution with test data:", part2_solution("day2_test_data.txt"))
    print("Part 2 solution with real data:", part2_solution("day2_data.txt"))
