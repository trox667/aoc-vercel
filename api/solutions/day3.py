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
            file = open('public/inputs/input03')
            return file.read()
        except Exception:
            return ''
    else:
        try:
            print('using http')
            response = requests.get(
                'https://aoc-trox667.vercel.app/inputs/input03')
            if response.status_code == 200:
                return response.text
        except Exception:
            return ''
    return ''


def file_to_bits():
    return [line.strip() for line in load_file().splitlines() if line.strip()]


def count_bits(index, bits_list):
    ones, zeroes = 0, 0
    for bits in bits_list:
        if bits[index] == '1':
            ones += 1
        else:
            zeroes += 1
    return ones, zeroes


def filter_bits(index, bits_list, b1='1', b2='0'):
    if len(bits_list) == 1:
        return bits_list
    a, b = count_bits(index, bits_list)
    if a > b or a == b:
        bits_list = list(filter(lambda b: b[index] == b1, bits_list))
    else:
        bits_list = list(filter(lambda b: b[index] == b2, bits_list))
    return bits_list


def part1():
    bits_list = file_to_bits()
    gamma, epsilon = '', ''
    for x in range(len(bits_list[0])):
        a, b = count_bits(x, bits_list)
        if a > b:
            gamma += '1'
            epsilon += '0'
        else:
            gamma += '0'
            epsilon += '1'

    return int(gamma, 2) * int(epsilon, 2)


def part2():
    bits_list = file_to_bits()
    oxygen_list = bits_list.copy()
    co2_scrubber_list = bits_list.copy()
    for x in range(len(bits_list[0])):
        oxygen_list = filter_bits(x, oxygen_list)
        co2_scrubber_list = filter_bits(x, co2_scrubber_list, '0', '1')

    return int(oxygen_list[0], 2) * int(co2_scrubber_list[0], 2)
