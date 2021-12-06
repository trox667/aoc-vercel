from collections import defaultdict

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
            file = open('public/inputs/input06')
            return file.read()
        except Exception:
            return ''
    else:
        try:
            print('using http')
            response = requests.get(
                'https://aoc-trox667.vercel.app/inputs/input06')
            if response.status_code == 200:
                return response.text
        except Exception:
            return ''
    return ''


def create_state():
    return list(map(int, load_file().split(',')))


def run(state, days=80):
    d = defaultdict(int)
    for s in state:
        d[s] += 1

    for day in range(0, days):
        count_new = d[0]
        d[0] = 0
        for i in range(1, 9):
            if d[i] > 0:
                d[i - 1] = d[i]
                d[i] = 0

        d[6] += count_new
        d[8] += count_new

    s = 0
    for v in d.values():
        s += v

    return s


def part1():
    return run(create_state())


def part2():
    return run(create_state(), 256)
