from abc import ABC, abstractmethod


class Day(ABC):
    @abstractmethod
    def part1(self):
        pass

    @abstractmethod
    def part2(self):
        pass
