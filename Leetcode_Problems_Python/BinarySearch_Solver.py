from Leetcode_Problems_Python.Solver_Interface import Solver
from typing import List


class BinarySearch_Sovler(Solver):

    def solve(self,  nums: List[int], target: int) -> int:

        # M: divide search space in half each iteration:
        i_s = 0
        i_e = len(nums)-1

        while i_s <= i_e:

            i_m = (i_e-i_s) // 2 + i_s  # M: Go into middle and divide space to left/right each iteration

            if nums[i_m] == target:
                return i_m
            if nums[i_m] > target:
                i_e = i_m -1
            if nums[i_m] <= target:
                i_s = i_m +1

        return -1


    def test_solve(self):
        nums = [-1,0,3,5,9,12]
        target = 9

        idx = self.solve(nums, target)
        print("Item was at idx: ", idx)