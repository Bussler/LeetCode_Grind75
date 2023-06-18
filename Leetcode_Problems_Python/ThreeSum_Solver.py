from Leetcode_Problems_Python.Solver_Interface import Solver
from typing import Optional, List
import re
from collections import OrderedDict
import math


def euclidian_distance(p1 : List[int], p2 : List[int]):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)


class ThreeSum_Solver(Solver):

    def solve(self, nums: List[int]) -> List[List[int]]:

        # Return all triplets that sum to 0 from nums

        # M: 1) Hashmap approach: store index to first two elements and remainder to 0 in hashmap -> Would need a lot of space tho for hashmap!
        # M: 2) Sorting approach: sort the nums. Pick first element and the move to pointers (large from right, small from left), till result is 0!
        # M: Avoid duplicates: Store valid results in set! In set each element is only present once
        
        target_sum = 0        
        nums.sort()
        
        store_set = set()
        
        for ptr_curr in range(len(nums)-2):
            
            ptr_left = ptr_curr+1
            ptr_right = len(nums)-1
            
            while ptr_left < ptr_right:
                
                cur_sum = nums[ptr_curr] + nums[ptr_left] + nums[ptr_right]
                
                if cur_sum == target_sum:
                    store_set.add((nums[ptr_curr], nums[ptr_left], nums[ptr_right]))
                    ptr_left += 1
                    ptr_right -= 1
                
                elif cur_sum > 0:
                    ptr_right -= 1
                    
                elif cur_sum < 0:
                    ptr_left += 1
            
        return list(store_set)

    def test_solve(self):

        nums = [-1,0,1,2,-1,-4]
        
        triplets = self.solve(nums)
        
        print("All zero triplets: ", triplets)
        