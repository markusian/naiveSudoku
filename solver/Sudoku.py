#!/usr/bin/env python
# -*- coding: utf-8 -*-
import numpy as np 

class Sudoku(object):
    """docstring for Sudoku"""
    def __init__(self, arg):
        super(Sudoku, self).__init__()
        self.arg = arg
        self.values = np.zeros()

        