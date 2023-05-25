from Leetcode_Problems_Python.Solver_Interface import Solver
import re


class Anagram_Sovler(Solver):

    def solve(self,  s: str, t: str) -> bool:
        
        # M: put all strings in a list, remove all elements from string from list
        #s_list = list(s)
        #for c in t:
        #    if c in s_list:
        #        s_list.remove(c)
        #    else:
        #        return False
        #return len(s_list) == 0
    
        if len(s) != len(t):
            return False

        # M: Increment/Decrement elements in hashtable: All have to be 0 in the end!
        h_table = {}
        for s_e, t_e in zip(s, t):

            if s_e not in h_table:
                h_table[s_e] = 1
            else:
                h_table[s_e] += 1

            if t_e not in h_table:
                h_table[t_e] = -1
            else:
                h_table[t_e] -= 1

        for entry in h_table.values():
            if entry != 0:
                return False
        return True


    def test_solve(self):
        s = "anagram"
        t = "nagaram"

        is_a = self.solve(s,t)
        print("Is Palindrome: ", is_a)