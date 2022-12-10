import aoc_helper
import numpy as np
from aoc_helper import (
    Grid,
    PrioQueue,
    decode_text,
    extract_ints,
    frange,
    irange,
    iter,
    list,
    map,
    range,
    tail_call,
)


def is_visible(trees, tree):
    if all(i < tree for i in trees):
        return True
    else:
        return False


def viewing_distance(trees, tree):
    distance = 0
    # print(trees)
    for t in trees:
        if t < tree:
            distance += 1
        else:
            distance += 1
            break
    # print(distance, tree, trees.size)
    # print(distance)

    return distance


def parse_raw(raw):
    lines = raw.split("\n")
    lines = [[*line] for line in lines]
    lines = [[int(c) for c in line] for line in lines]
    lines = np.array(lines)
    # print(lines.shape)
    return lines


def part_one(data):
    visible = 0
    for i, row in enumerate(data):
        for j, char in enumerate(row):
            left_row = row[:j]
            right_row = row[j + 1:]
            top = data[:i, j]
            bottom = data[i + 1:, j]
            if is_visible(left_row, char):
                visible += 1
                # print(left_row)
                # print("Visible from left", i, j, char)
            elif is_visible(right_row, char):
                visible += 1
                # print("Visible from right", i, j, char)
            elif is_visible(top, char):
                visible += 1
                # print("Visible from top", i, j, char)
            elif is_visible(bottom, char):
                visible += 1
                # print("Visible from bottom", i, j, char)

    return visible


def part_two(data):
    max_distances = []
    for i, row in enumerate(data):
        for j, char in enumerate(row):
            left_row = row[:j]
            right_row = row[j + 1:]
            top = data[:i, j]
            bottom = data[i + 1:, j]
            # print(bottom, np.flip(top))
            vision_left = viewing_distance(np.flip(left_row), char)
            vision_right = viewing_distance(right_row, char)
            vision_top = viewing_distance(np.flip(top), char)
            vision_bottom = viewing_distance(bottom, char)
            vision_score = vision_top * vision_left * vision_right * vision_bottom
            max_distances.append(vision_score)

    return max(max_distances)


if __name__ == '__main__':
    raw = aoc_helper.fetch(8, 2022)
    data = parse_raw(raw)
    # print(data)
    # print(data.shape)
    # print(part_two(data))

    # aoc_helper.lazy_test(day=8, year=2022, parse=parse_raw, solution=part_one)
    # aoc_helper.lazy_test(day=8, year=2022, parse=parse_raw, solution=part_two)
    aoc_helper.lazy_submit(day=8, year=2022, solution=part_one, data=data)
    aoc_helper.lazy_submit(day=8, year=2022, solution=part_two, data=data)
