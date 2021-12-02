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


def file_to_commands():
    return [(line.strip().split(' ')[0], int(line.strip().split(' ')[1])) for
            line
            in load_file().splitlines() if
            line.strip()]


def part1():
    actions = {'forward': lambda x, y, step: (x + step, y),
               'down': lambda x, y, step: (x, y + step),
               'up': lambda x, y, step: (x, y - step)}
    x, y = 0, 0
    for (command, step) in file_to_commands():
        x, y = actions[command](x, y, step)
    return x * y


def part2():
    actions = {
        'forward': lambda x, y, step, aim: (x + step, y + step * aim, aim),
        'down': lambda x, y, step, aim: (x, y, aim + step),
        'up': lambda x, y, step, aim: (x, y, aim - step)}
    x, y, aim = 0, 0, 0
    for (command, step) in file_to_commands():
        x, y, aim = actions[command](x, y, step, aim)
    return x * y
