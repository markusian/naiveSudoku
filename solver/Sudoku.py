#!/usr/bin/env python
# -*- coding: utf-8 -*-
import numpy as np

test_sudoku = """400000805
030000000
000700000
020000060
000080400
000010000
000603070
500200000
104000000"""

test_sudoku2 = """060030008
000000207
001805006
000607809
050409010
407301000
500904300
309000000
700010060"""

test_sudoku3 = """020000090
130000057
004080600
000306000
003020100
000901000
006050800
950000063
070000040"""

class Sudoku(object):

    """docstring for Sudoku"""

    def __init__(self):
        super(Sudoku, self).__init__()
        self.values = np.zeros([9, 9])
        self.possibles = {}
        self.incomplete = set([])
        self.parse()

    def parse(self):
        for x, line in enumerate(test_sudoku2.splitlines()):
            for y, val in enumerate(line):
                value = int(val)
                self.values[x, y] = value
                if value == 0:
                    self.possibles[x, y] = set(range(1, 10))
                    self.incomplete.add((x, y))

    def block_neighbours(self, x, y):
        """Return the list of the neighbours of the cell in the same block.
        """
        startX = x / 3 * 3
        startY = y / 3 * 3
        lis = [(a, b) for a in range(startX, startX + 3)
               for b in range(startY, startY + 3)]
               # TODO: eventually remove elements on the same column and row
        lis.remove((x, y))
        return lis

    def neighbours_values(self, x, y):
        """ Returns the list of all values set for the cells in the same block
        """
        val_block = set([self.values[a, b]
                         for (a, b) in self.block_neighbours(x, y)])
        # we can delete this last condition
        val_row = set([self.values[x, b] for b in range(9) if b != y])
        val_column = set([self.values[a, y] for a in range(9) if a != x])

        val_all = (val_block | val_row | val_column) - set([0])
        return val_all

    def block_possibles(self, x, y):
        """ Returns the union of the lists of all possible values for all the 
        cells in the same block
        """
        neighbours = self.block_neighbours(x, y)
        p = set()
        for neighbour in neighbours:
            xn, yn = neighbour
            try:
                p = p | self.possibles[xn, yn]
            except:
                pass
        return p

    def is_valid(self):
        """ Returns true if the sudoku is valid. The check is done lazily
        """
        if len(self.incomplete) !=0:
            return False
        else:
            sum_column = set(self.values.sum(0))
            sum_rows = set(self.values.sum(0))
            sums = sum_column | sum_rows 
            if sums == set([45]):
                return True
            else:
                return False 

    def __getitem__(self, pos):
        x, y = pos
        return self.values[x, y]

    def __setitem__(self, pos, value):
        x, y = pos
        self.values[x, y] = value

    def __repr__(self):
        s = ""
        for x in range(9):
            for y in range(9):
                s += str(int(self.values[x, y])
                         if self.values[x, y] != 0 else ".")
                s += " "
                if y == 2 or y == 5:
                    s += "| "
            s += "\n"
            if x == 2 or x == 5:
                s += "------+-------+-------" + "\n"
        return s
