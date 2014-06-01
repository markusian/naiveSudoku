#!/usr/bin/env python
# -*- coding: utf-8 -*-

from solver.Sudoku import Sudoku
from solver.SudokuSolver import NaiveSolver


sudoku = Sudoku()
solver = NaiveSolver(sudoku)

solver.solve()

