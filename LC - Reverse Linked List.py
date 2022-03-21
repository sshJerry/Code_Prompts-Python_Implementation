# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


#Iterative Method | Runtime: 40 ms    | Memory Usage: 15.4 MB
"""
Reverse Linked List - Iterative - Flow
head = [Null,1,2,3,4,5]         1st     2nd     3rd     4th     5th

temp = current.next             (2)     (3)     (4)     (5)     (null)
current.next = previous         (Null)  (1)     (2)     (3)     (4)
previous = current              (1)     (2)     (3)     (4)     (5)
current = temp                  (2)     (3)     (4)     (5)     (null)
"""

class Solution(object):
    def reverseList(self, head):
        previous = None
        current = head
        while current != None:
            temp = current.next
            current.next = previous
            previous = current
            current = temp
        return previous

#Recursive Method | Runtime: 28 ms    | Memory Usage: 18.7 MB
"""
Reverse Linked List - Recursive - Flow

head = [Null,1,2,3]
newH = curr (1)
newH = self._reverse(curr.next) (2)
        |___newH = curr(2)
            newH = self._reverse(curr.next) (3)
                                    |___newH = curr(3)
                                        curr.next = None
                                        return newH(3)
                                    ____|
            newH = 3 *FROM RETURN
            curr.next.next (3-->None) = curr(2) *SO 3-->2
            curr.next(2-->None)
            return newH(3-->2)
        ____|
newH = 3 *FROM RETURN
curr.next.next(2-->None) = curr(1) *SO 2-->1
curr.next(1-->None)
return newH(3-->2-->1-->None/Null)
"""

class Solution(object):
    def reverseList(self, head):
        if head is None:
            return head
        return self._reverse(head)

    def _reverse(self, curr):
        newH = curr
        if curr is None: return None

        if curr.next:
            newH = self._reverse(curr.next)
            curr.next.next = curr
        curr.next = None
        return newH
