from Leetcode_Problems_Python.Solver_Interface import Solver
import re


class Ransomnote_Sovler(Solver):

    def solve(self, ransomNote: str, magazine: str) -> bool:

        h_table = {}

        # M: Fill hashtable with letters from magazine
        for elem in magazine:
            if elem not in h_table:
                h_table[elem] = 1
            else:
                h_table[elem] += 1

        # M: check hashtable, if we have enough letters stored
        for elem in ransomNote:
            if elem not in h_table or h_table[elem] == 0:
                return False
            else:
                h_table[elem] -= 1

        return True

    def test_solve(self):
        ransomnote = "aa"
        magazing = "aab"

        can_construct = self.solve(ransomnote, magazing)
        print("Can construct note from magazin: ", can_construct)