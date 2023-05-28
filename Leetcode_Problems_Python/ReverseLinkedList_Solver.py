from Leetcode_Problems_Python.Solver_Interface import Solver
from typing import Optional
import re

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class ReversedLinkedList_Sovler(Solver):

    # M: Palindrome: word is same front/ backwards. Count letters that are present multiple times and one that is present once
    def solve(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if head is None or head.val is None:
            return None

        cur = head
        reversed_list = ListNode(cur.val)
        while cur.next is not None:
            helper = ListNode(cur.next.val, reversed_list)
            reversed_list = helper

            cur = cur.next

        return reversed_list

    def test_solve(self):
        #s = "abccccdd"
        s = "ccca"

        longestPalindrome = self.solve(s)
        print("Longest Palindrome with ", s, " : ", longestPalindrome)