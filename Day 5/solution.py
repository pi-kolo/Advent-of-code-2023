import re
from dataclasses import dataclass


@dataclass
class FactorMaping:
    destination_start: int
    source_start: int
    range_length: int

    def in_range(self, value):
        return value >= self.source_start and value < self.source_start + self.range_length
    
    def mapped_destination(self, value):
        return self.destination_start + (value - self.source_start)
    
    def __repr__(self) -> str:
        return f'({self.destination_start}, {self.source_start}, {self.range_length})'

    def __str__(self):
        return f'({self.destination_start}, {self.source_start}, {self.range_length})'


regex = r"seeds: ([0-9 ]*)\n\n" + \
    r"seed-to-soil map:\n([0-9 \n]*)\n" + \
    r"soil-to-fertilizer map:\n([0-9 \n]*)\n" + \
    r"fertilizer-to-water map:\n([0-9 \n]*)\n" + \
    r"water-to-light map:\n([0-9 \n]*)\n" + \
    r"light-to-temperature map:\n([0-9 \n]*)\n" + \
    r"temperature-to-humidity map:\n([0-9 \n]*)\n" + \
    r"humidity-to-location map:\n([0-9 \n]*)"
    

def parse_input(filename):
    with open(filename) as f:
        seeds, *data = re.search(regex, f.read()).groups()

        seeds = [int(seed) for seed in seeds.strip().split(' ')]
        factors_maps = [
            [FactorMaping(*[int(el) for el in line.strip().split(' ')]) for line in factor_map.strip().split('\n')] for factor_map in data
        ]

        return seeds, factors_maps


def find_seeds_factors(factors_maps: list[list[FactorMaping]], seeds):
    seeds_treatment = [[seed] for seed in seeds]
    for factor in factors_maps:
        for idx, seed in enumerate(seeds_treatment):
            current_maping = seed[-1]
            for factor_condition in factor:
                if factor_condition.in_range(current_maping):
                    next_factor = factor_condition.mapped_destination(current_maping)
                    seeds_treatment[idx].append(next_factor)
                    break
            else:
                seeds_treatment[idx].append(current_maping)
    return seeds_treatment
        

def find_seeds_factors_by_ranges(factors_maps: list[list[FactorMaping]], seeds):
    seeds_ranges = [(seeds[i], seeds[i] + seeds[i+1] - 1) for i in range(0, len(seeds) - 1, 2)]
    ranges = [seeds_ranges]
    for factor in factors_maps:
        factor_ranges = ranges[-1]
        new_ranges = []
        while len(factor_ranges) > 0:
            current_range = factor_ranges.pop(0)
            for condition in factor:
                if condition.in_range(current_range[0]) and condition.in_range(current_range[1]):
                    new_ranges.append((condition.mapped_destination(current_range[0]), condition.mapped_destination(current_range[1])))
                    break
                elif condition.in_range(current_range[0]) and not condition.in_range(current_range[1]):
                    new_ranges.append((condition.mapped_destination(current_range[0]), condition.destination_start + condition.range_length - 1))
                    factor_ranges.append((condition.source_start + condition.range_length, current_range[1]))
                    break
                elif not condition.in_range(current_range[0]) and condition.in_range(current_range[1]):
                    new_ranges.append((condition.destination_start, condition.mapped_destination(current_range[1])))
                    factor_ranges.append((current_range[0], condition.source_start - 1))
                    break
            else:
                new_ranges.append(current_range)
        ranges.append(new_ranges)
    return new_ranges
                

seeds, factors_maps = parse_input('input.txt')
seeds_factors = find_seeds_factors(factors_maps, seeds)

# find lowest last value
print(min([el[-1] for el in seeds_factors]))

#find lowest last value considering ranges as input
print(min(find_seeds_factors_by_ranges(factors_maps, seeds), key=lambda x: x[0])[0])

