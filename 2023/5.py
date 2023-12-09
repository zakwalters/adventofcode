from utils import *

example = """seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4
"""

def process_map(map_lines):
  return [tuple(map(lambda s: int(s), line.split())) for line in map_lines if line != ""]

def get_dest(source, mapping):
  for dest_start, source_start, range_len in mapping:
    if source >= source_start and source < (source_start + range_len):
      return dest_start + (source - source_start)
  else:
    return source

def part_one():
  input_file = get_input(5, False)
  sections = input_file.split('\n\n')
  seeds = list(map(lambda s: int(s), sections.pop(0).split()[1:]))

  mappings = {}
  for section in sections:
    heading, *lines = section.split('\n')
    name = heading.split()[0]
    mappings[name] = process_map(lines)

  locations = []
  for seed in seeds:
    soil = get_dest(seed, mappings["seed-to-soil"])
    fertilizer = get_dest(soil, mappings["soil-to-fertilizer"])
    water = get_dest(fertilizer, mappings["fertilizer-to-water"])
    light = get_dest(water, mappings["water-to-light"])
    temperature = get_dest(light, mappings["light-to-temperature"])
    humidity = get_dest(temperature, mappings["temperature-to-humidity"])
    location = get_dest(humidity, mappings["humidity-to-location"])
    locations.append(location)
  return min(locations)

def part_two():
  input_file = get_input(5, False)
  sections = input_file.split('\n\n')
  seeds_numbers = list(map(lambda s: int(s), sections.pop(0).split()[1:]))
  for i in range(0, len(seeds_numbers), 2):
    print(f"{i}:\t{seeds_numbers[i]}\t{seeds_numbers[i+1]}")

  mappings = {}
  for section in sections:
    heading, *lines = section.split('\n')
    name = heading.split()[0]
    mappings[name] = process_map(lines)

  locations = []
  for i in range(0, len(seeds_numbers), 2):
    for seed in range(seeds_numbers[i], seeds_numbers[i] + seeds_numbers[i + 1]):
      soil = get_dest(seed, mappings["seed-to-soil"])
      fertilizer = get_dest(soil, mappings["soil-to-fertilizer"])
      water = get_dest(fertilizer, mappings["fertilizer-to-water"])
      light = get_dest(water, mappings["water-to-light"])
      temperature = get_dest(light, mappings["light-to-temperature"])
      humidity = get_dest(temperature, mappings["temperature-to-humidity"])
      location = get_dest(humidity, mappings["humidity-to-location"])
      locations.append(location)
    print("Finished seed", i, 'found', len(locations), 'locations')
  return min(locations)

print(f"Part 1: {part_one()}")
print(f"Part 2: {part_two()}")
