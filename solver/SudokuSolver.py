#!/usr/bin/env python
# -*- coding: utf-8 -*-

#from Sudoku import Sudoku


class SudokuSolver(object):
    """Base class for the sudoku solvers"""

    def __init__(self, sudoku):
        super(SudokuSolver, self).__init__()
        self.sudoku = sudoku



class NaiveSolver(SudokuSolver):
    """Naive version of the solver"""
    def __init__(self, sudoku):
        super(NaiveSolver, self).__init__(sudoku)

    def print_possible(self):
        """ Prints the list of possible values for all the empty cells,
        together with the union of the possible values of all the other empty
        cells in the same block """
        lis = [(x, y) for x in range(9) for y in range(9)]
        for x, y in lis:
            if (x, y) in self.sudoku.possibles:
                pos = self.sudoku.possibles[x, y]
                block_pos = self.sudoku.block_possibles(x, y)
                print str((x, y)) + " " + str(pos),
                print "\t" * 3 + str(block_pos)

    def solve(self):
        """Solving function"""
        cycle = 0
        while len(self.sudoku.incomplete) != 0:
            print "Cycle: " + str(cycle)

            found = False
            cycle += 1
            completed = set()
            for cell in self.sudoku.incomplete:
                x, y = cell

                if len(self.sudoku.possibles[x, y]) == 1:
                    val = self.sudoku.possibles[x, y].pop()
                    self.sudoku[x, y] = val
                    self.sudoku.possibles.pop((x, y))
                    completed.add((x, y))
                    found = True
                else:
                    vals = set(self.sudoku.neighbours_values(x, y))
                    self.sudoku.possibles[x, y] -= vals

            self.sudoku.incomplete -= completed

            for cell in self.sudoku.incomplete:
                x, y = cell
                possibles = self.sudoku.possibles[x, y]
                block_possibles = self.sudoku.block_possibles(x, y)
                vals = self.sudoku.neighbours_values(x, y)

                # possible values for the cell, that are not also possible for
                # all the other cells in the block
                # we need to remove also vals, because otherwise there could be
                # some values set in this cycles that were not deleted from the possibles list 
                #of the other cells
                
                diff = possibles - vals - block_possibles
                if len(diff) == 1:
                    #print "Diff", (x, y), possibles, block_possibles
                    self.sudoku.possibles[x, y] = diff
                    found = True

            #self.print_possible()
            if found == False:
                print "Error"
                break

            print self.sudoku
            print "Valid? ", self.sudoku.is_valid()
            #raw_input()        
        