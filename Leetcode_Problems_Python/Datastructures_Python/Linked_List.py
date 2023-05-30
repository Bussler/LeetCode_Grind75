from typing import Optional, List

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
    def printList(self):
        elements = []
        head = self
        while head is not None:
            elements.append(head.val)
            head = head.next
        print(elements)
        
    @classmethod
    def create_LinkedList_from_List(cls, nodes: List):

        prev_elem = None
        for elem in reversed(nodes):
            prev_elem = ListNode(val=elem, next=prev_elem)
            
        return prev_elem
        
        
def create_test_list() -> ListNode:
    nodes = [1,2,3,4,5]
    return ListNode.create_LinkedList_from_List(nodes)
 