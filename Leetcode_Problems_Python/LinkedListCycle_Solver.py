from Leetcode_Problems_Python.Solver_Interace import Solver
from typing import List, Tuple, Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class LinkedListCycle_Solver(Solver):

    def solve(self,  head: Optional[ListNode]) -> bool:

        # M: vlt nodes eindeutig über val und next identifizieren?

        if head == None:
            return False

        ht = {}
        cur = head
        while True:
            cur_id = id(cur)
            if cur_id not in ht:
                ht[cur_id] = 1
            else:
                return True
            
            if cur.next == None:
                break
            cur = cur.next

        return False

    def test_solve(self):


        pass