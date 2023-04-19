from Leetcode_Problems_Python.Solver_Interace import Solver
import re


class Palindrome_Sovler(Solver):

    def solve(self, s: str) -> bool:
        
        # M: remove all non-alphabetic characters
        s_alpha_only_lower = re.sub(r'[^a-zA-Z0-9]', '', s).lower()

        p_l = 0
        p_r = len(s_alpha_only_lower)-1

        while (p_l<p_r):
            if s_alpha_only_lower[p_l] == s_alpha_only_lower[p_r]:
                p_l += 1
                p_r -= 1
            else:
                return False

        return True


    def test_solve(self):
        s = "A man, a plan, a canal: Panama"

        is_p = self.solve(s)
        print("Is Palindrome: ", is_p)