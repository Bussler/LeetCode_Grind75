from Leetcode_Problems_Python.Solver_Interface import Solver
from typing import Optional, List
import re 
from .Datastructures_Python.Linked_List import ListNode, create_test_list



class MiddleLinkedList_Solver(Solver):

    def solve(self, head: Optional[ListNode]) -> Optional[ListNode]:

        # M: Simple Idea: Traverse twice, once to get length of list, then to get middle node
        
        # M: More sophisticated: Use 2 pointers. Slow and Fast -> When Fast is at end of list, slow is in the middle!
        
        fast = head
        slow = head
        
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

        return slow

    def test_solve(self):
        test_list = create_test_list()
    
        middle_elem = self.solve(test_list)
        test_list.printList()
        print("Middle Elem: ", middle_elem.val)