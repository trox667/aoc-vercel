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


def file_to_depths():
    return [int(line.strip()) for line in load_file().splitlines() if
            line.strip()]


def count_increasing(depths, start=1):
    return sum([depths[i - start] < depths[i] for i in
                range(start, len(depths))])


def part1():
    return count_increasing(file_to_depths())


def part2():
    return count_increasing(file_to_depths(), 3)
