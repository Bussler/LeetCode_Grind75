from Leetcode_Problems_Python.Solver_Interace import Solver
from typing import List, Tuple


class FloodFill_Sovler(Solver):

    def fill(self, image: List[List[int]], sr: int, sc: int, color: int, starting_color: int):
        
        if sr < 0 or sr >= len(image) or sc < 0 or sc >= len(image[0]):
            return

        if image[sr][sc] != starting_color:  # M: For recusrsive calls: check if legal in beginning!
            return

        image[sr][sc] = color

        self.fill(image, sr, sc-1, color, starting_color)
        self.fill(image, sr-1, sc, color, starting_color)
        self.fill(image, sr, sc+1, color, starting_color)
        self.fill(image, sr+1, sc, color, starting_color)


    def solve(self,  image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:

        # M: Starting from sr, sc: Change all pixels in 4 dims with same color than starting pixel to desired color!
        # M: put new blocks in a list and put already treated blocks in a list: So that we dont look at blocks twice
        # M: recursive?

        if image[sr][sc] == color:
            return image

        self.fill(image, sr, sc, color, image[sr][sc])

        return image

    def test_solve(self):
        image = [[1,1,1],[1,1,0],[1,0,1]]
        sr = 1
        sc = 1
        color = 2

        res = self.solve(image, sr, sc, color)
        print(res)

        pass