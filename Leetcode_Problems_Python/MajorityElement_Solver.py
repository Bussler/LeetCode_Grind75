from Leetcode_Problems_Python.Solver_Interface import Solver
from typing import Optional, List
import re 



class MajorityElement_Sovler(Solver):

    # M: Palindrome: word is same front/ backwards. Count letters that are present multiple times and one that is present once
    def solve(self, nums: List[int]) -> int:

        # M: Idea: Hashing?
        # M: Better: Boyer-Moore Voting Algorithm: Increment if candidate is current element, decr otherwise -> Get element with n/2 occurances in the end
        
        candidate = None
        count = 0
        
        for elem in nums:
            if count == 0:
                candidate = elem
                count = 1
            else:
                if candidate == elem:
                    count += 1
                else:
                    count -= 1
        
        return candidate

    def test_solve(self):
        nums = [3,3,4]
    
        majorityElement = self.solve(nums)
        print("Majority Element ", majorityElement)