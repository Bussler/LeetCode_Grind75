from Leetcode_Problems_Python.Solver_Interface import Solver
import re


class Different_Sum_Sovler(Solver):

    stash = {}

    def climb_stairs(self, n: int):
       
        if n <= 2:
            return n
        
        if self.stash[n]!=-1: 
          return self.stash[n]; 
        
        self.stash[n]=self.climb_stairs(n-1)+self.climb_stairs(n-2)
        return self.stash[n]


    def solve(self, n: int) -> int:

        if n<=2:
            return n
        
        # M: store sub-results of all the different trees in a hashtable/list, so that we can easily use the results of that subtree, if it was computed before!
        self.stash = [-1] * (n+1)
        
        return self.climb_stairs(n)

    # M: Example:
    #           3
    #       2       1
    #   1     0  0  -1
    # 0  -1

    def solve_slow_recusrive(self, n: int) -> int:

        if n == 0: # M: valid solution
            return 1
        if n < 0: # M: invalid solution
            return 0
        
        # M: walk down tree/ stairs: go 1 or 2 steps
        return self.solve_slow_recusrive(n-1) + self.solve_slow_recusrive(n-2)

    def test_solve(self):
        n = 5

        diff_approaches = self.solve(n)
        print("Different approaches to sum: ", n, " : ", diff_approaches)