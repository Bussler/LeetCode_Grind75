from Leetcode_Problems_Python.Solver_Interface import Solver
from typing import List


class Stock_Sovler(Solver):

    def solve(self, prices: List[int]) -> int:

        left = 0
        right = left + 1
        hp = 0

        while right < len(prices):
            gain = prices[right] - prices[left]
            
            if prices[left] < prices[right]:
                hp = max(gain, hp) # M: If we get profit, compare it with previous best profit
            else:
                left = right # M: put the left pointer on the smallest element in the list for efficient comparisons

            right += 1
            
        return hp
    
    def solve_simple(self, prices: List[int]) -> int:

        # M: o(n^2): go over list from start to finish, store biggest difference
        hp = 0
        for i in range(len(prices)):
            curr_elem = prices[i]
            for elem in prices[i+1:]:
                gain = elem - curr_elem
                if hp < gain:
                    hp = gain

        return hp


    def test_solve(self):
        #prices = [1,2]
        prices = [7,1,5,3,6,4]

        best_val = self.solve(prices)
        print("Best Value: ", best_val)