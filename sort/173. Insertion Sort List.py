#
# Sort a linked list using insertion sort.
#
# Example
# Example 1:
# 	Input: 0->null
# 	Output: 0->null
#
#
# Example 2:
# 	Input:  1->3->2->0->null
# 	Output :0->1->2->3->null


"""
Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""


class Solution:
    """
    @param head: The first node of linked list.
    @return: The head of linked list.
    """

    def insertionSortList(self, head):
        # write your code here
        dummy = ListNode(0, head)
        current_end = head

        while current_end.next:
            target_val = current_end.next.val
            if current_end.val < current_end.next.val:
                current_end = current_end.next
            else:
                compared_node = dummy
                while (compared_node != current_end):
                    if compared_node.next.val < target_val:
                        compared_node = compared_node.next
                    else:
                        tmp = compared_node.next
                        cnn = current_end.next.next
                        compared_node.next = current_end.next
                        current_end.next = cnn
                        compared_node.next.next = tmp
                        break
        return dummy.next
