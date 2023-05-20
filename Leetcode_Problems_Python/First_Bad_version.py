from Leetcode_Problems_Python.Solver_Interace import Solver
from typing import List, Tuple, Optional
import random

GLOBAL_CORRECT = -1

def isBadVersion(version: int) -> bool:
    if GLOBAL_CORRECT == -1:
        return random.choice([True, False])
    else:
        return version == GLOBAL_CORRECT


class FirstBadVersion_Solver(Solver):

    def solve(self, n: int) -> int:
        
        # M: Use solution of binary search: convere left and right pointer and minimize calls to 'isBadVersion'
        # Example: 1 2 3 4b 5

        i_s = 1
        i_e = n

        while i_s < i_e:

            i_m = (i_e-i_s) // 2 + i_s  # M: Go into middle and divide space to left/right each iteration

            if isBadVersion(i_m): # M: Search right
                i_e = i_m
            else: #M: Search left
                i_s = i_m + 1

        return i_s


    def test_solve(self):
        n = 5
        global GLOBAL_CORRECT
        GLOBAL_CORRECT = 4

        first_bad = self.solve(n)
        print("FirstBadVersion: ", first_bad)

        pass