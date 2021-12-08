from collections import Counter
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
    line_tokens = [line.strip().split('|') for line in load_file().splitlines()
                   if
                   line.strip()]
    lines = []
    for line in line_tokens:
        a = line[0].strip().split()
        b = line[1].strip().split()
        lines.append((a, b))
    return lines


def determine_digit(one, four, seven, eight, rest):
    segment = ['-', '-', '-', '-', '-', '-', '-']
    segment[2] = one[0]
    segment[5] = one[1]

    sr = list(filter(lambda c: c not in segment, seven))
    segment[0] = sr[0]

    fr = list(filter(lambda c: c not in segment, four))
    segment[1] = fr[0]
    segment[3] = fr[1]

    fe = list(filter(lambda c: c not in segment, eight))
    segment[4] = fe[0]
    segment[6] = fe[1]

    lf = filter(lambda word: len(word) == 5, rest)
    ls = filter(lambda word: len(word) == 6, rest)
    lf_counter = Counter(''.join(lf))
    ls_counter = Counter(''.join(ls))

    if lf_counter[segment[1]] != 1:
        segment[1], segment[3] = segment[3], segment[1]

    if ls_counter[segment[2]] != 2:
        segment[2], segment[5] = segment[5], segment[2]

    if ls_counter[segment[4]] != 2:
        segment[4], segment[6] = segment[6], segment[4]

    return segment


def digit_from_segment(word, segment):
    digits = [[0, 1, 2, 4, 5, 6],  # 0
              [2, 5],  # 1
              [0, 2, 3, 4, 6],  # 2
              [0, 2, 3, 5, 6],  # 3
              [1, 2, 3, 5],  # 4
              [0, 1, 3, 5, 6],  # 5
              [0, 1, 3, 4, 5, 6],  # 6
              [0, 2, 5],  # 7
              [0, 1, 2, 3, 4, 5, 6],  # 8
              [0, 1, 2, 3, 5, 6]]  # 9

    for i in range(len(digits)):
        digit = digits[i]
        if len(digit) != len(word):
            continue
        s = ""
        for d in digit:
            s += segment[d]
        if Counter(word) == Counter(s):
            return str(i)

    return ""


def part1():
    lines = create_input()
    count_unique = 0
    for line in lines:
        for word in line[1]:
            if len(word) in {2, 3, 4, 7}:
                count_unique += 1
    return count_unique


def part2():
    result = 0
    lines = create_input()
    one, four, seven, eight = '-', '-', '-', '-'
    for line in lines:
        rest = []
        for word in line[0]:
            if len(word) == 2:
                one = word
            elif len(word) == 3:
                seven = word
            elif len(word) == 4:
                four = word
            elif len(word) == 7:
                eight = word
            else:
                rest.append(word)
        segment = determine_digit(one, four, seven, eight, rest)
        number = ""
        for word in line[1]:
            number += digit_from_segment(word, segment)
        result += int(number)
    return result
