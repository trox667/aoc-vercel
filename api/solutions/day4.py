import requests
import os
from dotenv import load_dotenv


def is_debug():
    load_dotenv()
    DEBUG = os.getenv('AOC_DEBUG')
    print('AOC_DEBUG', DEBUG)
    return DEBUG is not None


def load_file():
    if is_debug():
        try:
            print('using local file')
            file = open('public/inputs/input04')
            return file.read()
        except Exception:
            return ''
    else:
        try:
            print('using http')
            response = requests.get(
                'https://aoc-trox667.vercel.app/inputs/input04')
            if response.status_code == 200:
                return response.text
        except Exception:
            return ''
    return ''


def file_to_input():
    lines = [line.strip() for line in load_file().splitlines() if line.strip()]
    return lines[:1][0], lines[1:]


def get_board_input(lines):
    boards = []
    for i in range(0, len(lines), 5):
        boards.append(Board(lines[i:i + 5]))
    return boards


class Board:
    def __init__(self, lines):
        self.grid = []
        self.marker = set()
        self.last_marker = None
        self.completed = False

        for line in lines:
            row = []
            for word in line.split():
                row.append(int(word))
            self.grid.append(row)

    def mark(self, value):
        y = 0
        for row in self.grid:
            x = 0
            for v in row:
                if v == value:
                    self.marker.add((x, y))
                    self.last_marker = value
                x += 1
            y += 1

    def is_completed(self):
        for i in range(5):
            if (0, i) in self.marker and (1, i) in self.marker and (
                    2, i) in self.marker and (3, i) in self.marker and (
                    4, i) in self.marker:
                return True
            if (i, 0) in self.marker and (i, 1) in self.marker and (
                    i, 2) in self.marker and (i, 3) in self.marker and (
                    i, 4) in self.marker:
                return True
        return False

    def sum_unmarked(self):
        s = 0
        for y in range(5):
            for x in range(5):
                if (x, y) not in self.marker:
                    s += self.grid[y][x]
        return s


def part1():
    numbers, board_input = file_to_input()
    boards = get_board_input(board_input)
    for value in numbers.split(','):
        for board in boards:
            board.mark(int(value))
            if board.is_completed():
                return board.sum_unmarked() * board.last_marker


def part2():
    results = []
    numbers, board_input = file_to_input()
    boards = get_board_input(board_input)
    for value in numbers.split(','):
        for board in boards:
            if board.completed:
                continue
            board.mark(int(value))
            if board.is_completed():
                board.completed = True
                results.append(board.sum_unmarked() * board.last_marker)
    return results.pop()


print(part1())
print(part2())
