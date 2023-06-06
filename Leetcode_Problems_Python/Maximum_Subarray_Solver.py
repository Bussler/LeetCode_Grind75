from Leetcode_Problems_Python.Solver_Interface import Solver
from typing import Optional, List
import re 



class MaximumSubarray_Solver(Solver):

    def solve(self, nums: List[int]) -> int:

        # Holding 2 arrays:
        # 1: Best sum till now
        # 2: Best sum of prev sub array: decide if to expand sub array: Start new sub array, if curr number better single than combined with prev. Otherwise expand with cur number.
        
        stash = [[0]*len(nums) for i in range(2)]
        stash[1][0] = stash[0][0] = nums[0]
        
        for i in range(1, len(nums)):
            stash[1][i] = max(nums[i], nums[i] + stash[1][i-1])
            stash[0][i] = max(stash[0][i-1], stash[1][i])

        return stash[0][-1]

    def test_solve(self):
        nums = [-2,1,-3,4,-1,2,1,-5,4]
    
        largest_sum = self.solve(nums)
        print("Largest Sum: ", largest_sum)