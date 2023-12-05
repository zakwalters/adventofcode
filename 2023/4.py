import re
from utils import *

def part_one():
  lines = get_input(4)
  points = 0
  for line in lines:
    _game, card = re.split(r': ', line)
    winners_str, numbers_str = re.split(r' \| ', card)
    winners = list(map(lambda s: int(s), winners_str.split()))
    numbers = list(map(lambda s: int(s), numbers_str.split()))
    winning_numbers = len(list(filter(lambda n: n in winners, numbers)))
    if winning_numbers:
      points += 2 ** (winning_numbers - 1)
  return points

def part_two():
  lines = get_input(4)
  num_copies = { game_num: 1 for game_num in range(1, len(lines) + 1) }
  for game_num, line in enumerate(lines, 1):
    _game, card = re.split(r': ', line)
    winners_str, numbers_str = re.split(r' \| ', card)
    winners = list(map(lambda s: int(s), winners_str.split()))
    numbers = list(map(lambda s: int(s), numbers_str.split()))
    winning_numbers = len(list(filter(lambda n: n in winners, numbers)))
    for i in range(1, winning_numbers + 1):
      num_copies[game_num + i] += num_copies[game_num]
  return sum(num_copies.values())

print(f"Part 1: {part_one()}")
print(f"Part 2: {part_two()}")
