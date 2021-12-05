import requests
import os
from dotenv import load_dotenv
import re


def is_debug():
    load_dotenv()
    DEBUG = os.getenv('AOC_DEBUG')
    print('AOC_DEBUG', DEBUG)
    return DEBUG is not None


def load_file():
    if is_debug():
        try:
            print('using local file')
            file = open('public/inputs/input05')
            return file.read()
        except Exception:
            return ''
    else:
        try:
            print('using http')
            response = requests.get(
                'https://aoc-trox667.vercel.app/inputs/input05')
            if response.status_code == 200:
                return response.text
        except Exception:
            return ''
    return ''


class Line:
    def __init__(self, a, b, c, d):
        self.x1 = a
        self.y1 = b
        self.x2 = c
        self.y2 = d

    def __repr__(self):
        return f'({self.x1},{self.y1} -> {self.x2},{self.y2})'

    def range(self):
        if self.x1 <= self.x2:
            x_range = range(self.x1, self.x2 + 1)
        else:
            x_range = range(self.x1, self.x2 - 1, -1)

        if self.y1 <= self.y2:
            y_range = range(self.y1, self.y2 + 1)
        else:
            y_range = range(self.y1, self.y2 - 1, -1)

        return x_range, y_range

    def is_horizontal(self):
        return self.y1 == self.y2

    def is_vertical(self):
        return self.x1 == self.x2

    def is_diagonal(self):
        return abs(self.x1 - self.x2) == abs(self.y1 - self.y2)


def line_generator(lines, diagonal=False):
    for line in lines:
        x_range, y_range = line.range()
        if line.is_horizontal():
            for x in x_range:
                yield x, line.y1
        elif line.is_vertical():
            for y in y_range:
                yield line.x1, y
        elif diagonal and line.is_diagonal():
            for x, y in zip(x_range, y_range):
                yield x, y
        else:
            pass


def file_to_lines():
    p = re.compile('(\\d+),(\\d+) -> (\\d+),(\\d+)')
    matches = [p.findall(line) for line in load_file().splitlines()]
    lines = []
    assert len(matches) >= 1 and len(matches[0][0]) == 4
    for match in matches:
        lines.append(
            Line(int(match[0][0]), int(match[0][1]), int(match[0][2]),
                 int(match[0][3])))

    return lines


def part1():
    lines = file_to_lines()
    line_gen = line_generator(lines)
    visited = set()
    doubled = set()
    for coord in line_gen:
        if coord in visited:
            doubled.add(coord)
        else:
            visited.add(coord)
    return len(doubled)


def part2():
    lines = file_to_lines()
    line_gen = line_generator(lines, True)
    visited = set()
    doubled = set()
    for coord in line_gen:
        if coord in visited:
            doubled.add(coord)
        else:
            visited.add(coord)
    return len(doubled)
