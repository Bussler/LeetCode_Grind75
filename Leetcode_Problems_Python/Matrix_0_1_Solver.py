from Leetcode_Problems_Python.Solver_Interface import Solver
from typing import Optional, List
import re
from collections import OrderedDict
import math


class Matrix01_Solver(Solver):

    def solve(self, mat : List[List[int]]) -> List[List[int]] :

        # Given an m x n binary matrix mat, return the distance of the nearest 0 for each cell.
        # M: Dynamic Programming approach: No queue, we safe only the previous data
        # M: Do two passes: Update first elements left to right, top to bottom; then min right to left, bottom to top
        # M: That way we can be sure that all sides of a cell were at least once investigated and we have the shortest path
        # M: If we update all 4 sides at once we cant be sure that all 4 neighbours were already updated by closest neighbour!
        
        """
        |-1-1|-10|1 1
        |0 -1|0 0|0 1
        |1 -1|1 0|1 1 
        """
        
        for i in range(0, len(mat)):
            for j in range(0, len(mat[0])):
                if mat[i][j] != 0:
                    
                    top = math.inf
                    left = math.inf
                    
                    if i > 0:
                        top = mat[i-1][j]
                        
                    if j > 0:
                        left = mat[i][j-1]
                    
                    mat[i][j] = min(top, left) +1
                    
        for i in range(0, len(mat)):
            for j in range(0, len(mat[0])):
                if mat[i][j] != 0:
                    
                    bottom = math.inf
                    right = math.inf
                    
                    if i < len(mat)-1:
                        bottom = mat[i+1][j]
                        
                    if j < len(mat[0])-1:
                        right = mat[i][j+1]
                    
                    mat[i][j] = min(mat[i][j], bottom+1, right+1)

        return mat

    def test_solve(self):
        mat =[[0,0,1],[0,1,0],[1,1,1]]
        
        distance_mat = self.solve(mat)
        
        print("Output: ", distance_mat)
        