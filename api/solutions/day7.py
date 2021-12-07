import sys
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
            file = open('public/inputs/input07')
            return file.read()
        except Exception:
            return ''
    else:
        try:
            print('using http')
            response = requests.get(
                'https://aoc-trox667.vercel.app/inputs/input07')
            if response.status_code == 200:
                return response.text
        except Exception:
            return ''
    return ''


def create_input():
    return [int(t) for t in load_file().split(',')]


def part1():
    pos = create_input()
    end = max(pos)
    pos_set = range(0, end)
    min_f = sys.maxsize
    for h in pos_set:
        f = 0
        for p in pos:
            if p != h:
                f += abs(h - p)
        min_f = min(f, min_f)
    return min_f


def part2():
    pos = create_input()
    end = max(pos)
    pos_set = range(0, end)
    min_f = sys.maxsize

    visited = {}

    for h in pos_set:
        f = 0
        for p in pos:
            if p != h:
                d = abs(h - p)

                if d not in visited:
                    fc = sum([i for i in range(1, d + 1)])
                    visited[d] = fc
                    f += fc
                else:
                    f += visited[d]

                if f > min_f:
                    break
        min_f = min(f, min_f)
    return min_f
