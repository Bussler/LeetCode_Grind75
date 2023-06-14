from Leetcode_Problems_Python.Solver_Interface import Solver
from typing import Optional, List
import re
from collections import OrderedDict
import math


def euclidian_distance(p1 : List[int], p2 : List[int]):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)


class K_Closest_Points_Solver(Solver):

    def solve(self, points: List[List[int]], k: int) -> List[List[int]]:

        distances = []
        for elem in points:
            distance_origin = euclidian_distance(elem, [0,0])
            distances.append((elem, distance_origin))

        distances.sort(key= lambda x : x[1])
        closest_points = []
        
        for i in range(k):
            closest_points.append(distances[i][0])

        return closest_points

    def test_solve(self):

        #points = [[1,3],[-2,2]]
        #k = 1
        
        points = [[3,3],[5,-1],[-2,4]]
        k = 2
        
        nearest_points = self.solve(points,k)
        
        print("Nearest points: ", nearest_points)
        