from Leetcode_Problems_Python.Solver_Interface import Solver
import re


class LongestPalindrome_Sovler(Solver):

    # M: Palindrome: word is same front/ backwards. Count letters that are present multiple times and one that is present once
    def solve(self, s: str) -> int:

        h_table = {}
        for elem in s:
            if elem not in h_table:
                h_table[elem] = 1
            else:
                h_table[elem] += 1

        used_odd = False
        longest_Palindrome = 0

        for elem in h_table.values():
            if not used_odd and elem % 2 == 1:
                longest_Palindrome += elem
                used_odd = True
                continue
            if elem > 1:
                longest_Palindrome += (elem // 2) * 2
        return longest_Palindrome

    def test_solve(self):
        #s = "abccccdd"
        s = "ccca"

        longestPalindrome = self.solve(s)
        print("Longest Palindrome with ", s, " : ", longestPalindrome)