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
            file = open('public/inputs/input11')
            return file.read()
        except Exception:
            return ''
    else:
        try:
            print('using http')
            response = requests.get(
                'https://aoc-trox667.vercel.app/inputs/input11')
            if response.status_code == 200:
                return response.text
        except Exception:
            return ''
    return ''


def create_energy_map():
    data = load_file()
    return [[int(c) for c in line] for line in data.splitlines()]


def neighbors(x, y, width, height):
    n = [(x - 1, y - 1), (x, y - 1), (x + 1, y - 1), (x - 1, y), (x, y),
         (x + 1, y), (x - 1, y + 1), (x, y + 1), (x + 1, y + 1)]
    return list(filter(lambda t: 0 <= t[0] < width and 0 <= t[1] < height, n))


def update_all(energy_map):
    flash = []
    for y in range(len(energy_map)):
        for x in range(len(energy_map[0])):
            energy_map[y][x] += 1
            if energy_map[y][x] > 9:
                flash.append((x, y))
                energy_map[y][x] = 0
    return flash


def update_neighbors(neighbors, flashed, energy_map):
    flash = []
    for x, y in neighbors:
        if (x, y) not in flashed:
            energy_map[y][x] += 1
            if energy_map[y][x] > 9:
                flash.append((x, y))
                energy_map[y][x] = 0
    return flash


def sum_is_zero(energy_map):
    for y in range(len(energy_map)):
        for x in range(len(energy_map[0])):
            if energy_map[y][x] > 0:
                return False
    return True


def run(steps, energy_map):
    width = len(energy_map[0])
    height = len(energy_map)
    flash_counter = 0
    step_zero = None
    for step in range(steps):
        if sum_is_zero(energy_map):
            return None, step
        current_flashes = update_all(energy_map)
        skip_flashes = set(current_flashes)
        flash_counter += len(current_flashes)
        while len(current_flashes) > 0:
            x, y = current_flashes.pop(0)
            n = neighbors(x, y, width, height)
            n_flashes = update_neighbors(n, skip_flashes, energy_map)
            flash_counter += len(n_flashes)
            skip_flashes.update(n_flashes)
            current_flashes.extend(n_flashes)

    return flash_counter, step_zero


def part1():
    energy_map = create_energy_map()
    return run(100, energy_map)[0]


def part2():
    energy_map = create_energy_map()
    return run(1000, energy_map)[1]
