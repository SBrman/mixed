# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    extra = 0
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 == None and l2 == None:
            return ListNode(self.extra, None) if self.extra != 0 else None
        if l1 == None:
            l1 = ListNode(self.extra, None)
            self.extra = 0
        if l2 == None:
            l2 = ListNode(self.extra, None)
            self.extra = 0
        self.extra = int(s/10) if (s := l1.val+l2.val+self.extra) >= 10 else 0
        return ListNode(s-self.extra*10, self.addTwoNumbers(l1.next, l2.next))
    
def node(list1):
    # Make linked list and return head node
    if len(list1) == 1:
        return ListNode(list1.pop(0), None)
    Node = ListNode(list1.pop(0), node(list1))
    return Node

def printLinkedList(node):
    while node:
        print(node.val)
        node = node.next
    
    
list1 = [2,4,3]
list2 = [5,6,4]

Node1 = node(list1)
Node2 = node(list2)

##printLinkedList(Node1)
##printLinkedList(Node2)

Sol = Solution()
sumNodes = Sol.addTwoNumbers(Node1, Node2)
printLinkedList(sumNodes)
