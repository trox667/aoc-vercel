from functools import reduce

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
            file = open('public/inputs/input09')
            return file.read()
        except Exception:
            return ''
    else:
        try:
            print('using http')
            response = requests.get(
                'https://aoc-trox667.vercel.app/inputs/input09')
            if response.status_code == 200:
                return response.text
        except Exception:
            return ''
    return ''


POINTS_PT1 = {')': 3, '}': 1197, ']': 57, '>': 25137}
POINTS_PT2 = {')': 1, '}': 3, ']': 2, '>': 4}
CLOSING = [')', '}', ']', '>']
OPEN_CLOSING = {'(': ')', '{': '}', '[': ']', '<': '>'}
CLOSING_OPEN = {')': '(', '}': '{', ']': '[', '>': '<'}


class Stack:
    def __init__(self):
        self.data = []

    def add(self, value):
        self.data.append(value)

    def peek(self, i=-1):
        return self.data[i]

    def remove(self):
        return self.data.pop()

    def __len__(self):
        return len(self.data)

    def __repr__(self):
        return ','.join(self.data)


def get_chunks():
    data = load_file()
    return [line for line in data.splitlines()]


def parse(chunk):
    stack = Stack()
    stack.add(chunk[0])
    i = 1
    for c in chunk[1:]:
        if len(stack) > 0:
            if c in CLOSING and CLOSING_OPEN[c] == stack.peek():
                stack.remove()
            else:
                if c in CLOSING:
                    return i
                else:
                    stack.add(c)
            i += 1
    return None


def parse2(chunk):
    stack = Stack()
    stack.add(chunk[0])
    for c in chunk[1:]:
        closing = False
        if len(stack) > 0:
            if c in CLOSING and CLOSING_OPEN[c] == stack.peek():
                stack.remove()
                closing = True
            else:
                if c in CLOSING:
                    return []
        if not closing:
            stack.add(c)

    added = []
    while len(stack) > 0:
        c = stack.remove()
        added.append(OPEN_CLOSING[c])
    return added


def part1():
    points = 0
    chunks = get_chunks()
    for chunk in chunks:
        i = parse(chunk)
        if i is not None:
            points += POINTS_PT1[chunk[i]]
    return points


def part2():
    results = []
    chunks = get_chunks()
    for chunk in chunks:
        points = 0
        added = parse2(chunk)
        for a in added:
            points *= 5
            points += POINTS_PT2[a]
        if points > 0:
            results.append(points)
    results.sort()
    return results[len(results)//2]