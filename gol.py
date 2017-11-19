#!/usr/bin/python3


class Cell:
    def __init__(self, alive):
        self.alive = alive
        self.living_neighbours = 0

    def will_i_live(self):
        if (self.living_neighbours < 2 or self.living_neighbours > 3) and self.alive:
            return False
        elif (2 <= self.living_neighbours <= 3) and self.alive:
            return True

