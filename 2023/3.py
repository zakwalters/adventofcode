import re
from utils import *

example = """*467..114.
2..*......
..35..633.
......#...
617*......
.....+.58.
..592.....
755.......
*598$.*...
....664..."""

def part_one():
  lines = get_input(3)
  part_numbers = []
  for i, line in enumerate(lines):
    for match in re.finditer(r'\d+', line):
      start = match.start() - 1 if match.start() > 0 else 0
      end = match.end() + 1 if match.end() < len(line) else len(line)

      above = lines[i - 1][start:end] if i > 0 else ''
      left = line[match.start() - 1] if match.start() > 0 else ''
      right = line[match.end()] if match.end() < len(line) else ''
      below = lines[i + 1][start:end] if i < len(lines) - 1 else ''
      adjacents = above + left + right + below

      if re.search(r'[^\.\d]', adjacents):
        part_numbers.append(int(match.group()))

  return sum(part_numbers)

def part_two():
  lines = get_input(3)

  def star_is_adjacent(s, m):
    return s.start() >= m.start() - 1 and s.end() <= m.end() + 1

  gear_ratios = []
  for i, line in enumerate(lines):
    for star in re.finditer(r'\*', line):
      right_match = re.match(r'\d+', line[star.end():])
      n_right = right_match.group() if right_match is not None else None
      left_matches = list(re.finditer(r'\d+', line[:star.start()]))
      n_left = left_matches[-1].group() if len(left_matches) > 0 and left_matches[-1].end() == star.start() else None
      above_matches = re.finditer(r'\d+', lines[i - 1]) if i > 0 else []
      ns_above = list(match.group() for match in above_matches if star_is_adjacent(star, match) )
      below_matches = list(re.finditer(r'\d+', lines[i + 1]) if i < len(lines) - 1 else [])
      ns_below = list(match.group() for match in below_matches if star_is_adjacent(star, match))

      adjacent_numbers = list(map(lambda s: int(s), filter(lambda x: x is not None, [n_right, n_left] + ns_above + ns_below)))
      if len(adjacent_numbers) == 2:
        gear_ratios.append(adjacent_numbers[0] * adjacent_numbers[1])

  return sum(gear_ratios)

print(f"Part 1: {part_one()}")
print(f"Part 2: {part_two()}")
