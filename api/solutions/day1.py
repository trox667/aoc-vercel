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
            file = open('public/inputs/input01')
            return file.read()
        except Exception:
            return ''
    else:
        try:
            print('using http')
            response = requests.get(
                'https://aoc-trox667.vercel.app/inputs/input01')
            if response.status_code == 200:
                return response.text
        except Exception:
            return ''
    return ''


def count_increase(depths):
    increased_count = 0
    for i in range(1, len(depths)):
        if depths[i - 1] < depths[i]:
            increased_count += 1
    return increased_count


def part1():
    depths = [int(line.strip()) for line in load_file().splitlines() if
              line.strip()]
    return count_increase(depths)


def part2():
    depths = [int(line.strip()) for line in load_file().splitlines() if
              line.strip()]
    sums = []
    for i in range(0, len(depths) - 2):
        a = sum([depths[i + 0], depths[i + 1], depths[i + 2]])
        sums.append(a)

    return count_increase(sums)
