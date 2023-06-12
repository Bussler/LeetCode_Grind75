from Leetcode_Problems_Python.Solver_Interface import Solver
from typing import Optional, List
import re
from collections import OrderedDict


# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Clone_Graph_Solver(Solver):

    def solve(self,  node: Node) -> Node:

        # M: BFS to traverse graph, hashmap to keep track of already visited nodes
        
        if node == None:
            return None
        
        # M: Queue to handle bfs: push back newly visited nodes
        queue = [node]
        
        # M: Hashmap to hold clones of already visited nodes: we have to deep copy!
        clones = {node.val : Node(node.val, [])}
        
        while queue:
            cur_q = queue.pop(0)
            cur_clone = clones[cur_q.val]
            
            # M: traverse all neighbours
            for neighbour in cur_q.neighbors:
                # M: if we didnt look at that node yet: put into queue to be visited and create clone. Fill neighbour list of clone later
                if neighbour.val not in clones:
                    clones[neighbour.val] = Node(neighbour.val, [])
                    queue.append(neighbour)
                
                # M: build up the neighbourhood again
                cur_clone.neighbors.append(clones[neighbour.val])

        return clones[node.val]

    def test_solve(self):
        pass