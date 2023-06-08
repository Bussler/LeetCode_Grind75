from Leetcode_Problems_Python.Solver_Interface import Solver
from typing import Optional, List
import re
from collections import OrderedDict



class Longest_Substring_Solver(Solver):

    def solve(self,  s: str) -> int:

        # M: keep track of elements till now
        hash_set = set()
        
        # M: sliding window approach
        start = 0
        end = 0
        max_length = 0
        
        while end < len(s):
            elem = s[end]
            
            # M: if not repeating element: expand current substring
            if elem not in hash_set:
                hash_set.add(elem)
                end += 1
                max_length = max(max_length, end-start)
            # M: if repeating: remove char at start from stash and move start
            else:
                hash_set.remove(s[start])
                start += 1
            
        return max_length
    
    def solve_ordered_hashmap(self,  s: str) -> int:

        # M: keep track of elements till now: order elements fifo
        hash_set = OrderedDict()
        
        # M: sliding window approach
        start = 0
        end = 0
        max_length = 0
        
        while end < len(s):
            elem = s[end]
            
            # M: if not repeating element: expand current substring
            if elem not in hash_set:
                hash_set[elem] = end
                end += 1
                max_length = max(max_length, end-start)
            # M: if repeating: start sliding window from next char that is repeating
            else:
                start = hash_set[elem]+ 1
                
                # Find keys to remove: all prior to elem
                remove_elements = []
                for e in hash_set:
                    remove_elements.append(e)
                    if e == elem:
                        break
                for e in remove_elements:
                    del hash_set[e]
                
        return max_length

    def test_solve(self):
        s = "abcabcbb"
        s = "abba"
    
        length = self.solve(s)
        print("Length of longest substring: ", length)