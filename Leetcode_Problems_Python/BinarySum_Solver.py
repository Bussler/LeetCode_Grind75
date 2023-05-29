from Leetcode_Problems_Python.Solver_Interface import Solver
from typing import Optional, List
import re 



class BinarySum_Solver(Solver):

    def solve(self, a: str, b: str) -> str:

        # M: easy idea: convert str to int, add, return back to binary
        
        a_i = int(a,2)
        b_i = int(b,2)
        
        sum_i = a_i + b_i
        
        return format(sum_i, 'b')

    def test_solve(self):
        a = "1010"
        b = "1011"
    
        sum_res = self.solve(a,b)
        print("Sum: ", sum_res)