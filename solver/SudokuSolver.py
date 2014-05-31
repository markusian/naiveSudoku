#!/usr/bin/env python
# -*- coding: utf-8 -*-
from Sudoku import Sudoku


class SudokuSolver(object):
    """docstring for SudokuSolver"""
    def __init__(self, sudoku):
        super(SudokuSolver, self).__init__()
        self.sudoku = sudoku 
        