import re
from utils import *

str_to_int_mapping = {
  "one": 1,
  "two": 2,
  "three": 3,
  "four": 4,
  "five": 5,
  "six": 6,
  "seven": 7,
  "eight": 8,
  "nine": 9,
}

def str_to_int(n):
  try:
    return int(n)
  except ValueError:
    return str_to_int_mapping[n]

def part_one():
  lines = get_input(1)
  calibration_values = []
  for line in lines:
    digits = re.findall(r'\d', line)
    calibration_values.append(int(digits[0]) * 10 + int(digits[-1]))
  return sum(calibration_values)

def part_two():
  lines = get_input(1)
  calibration_values = []
  for line in lines:
    # This (?=()) business deals with overlapping matches: https://stackoverflow.com/a/5616910
    digits = re.findall(r'(?=(\d|one|two|three|four|five|six|seven|eight|nine))', line)
    int_digits = [str_to_int(d) for d in digits]
    calibration_values.append(int_digits[0] * 10 + int_digits[-1])
  return sum(calibration_values)

print(f"Part 1: {part_one()}")
print(f"Part 2: {part_two()}")
