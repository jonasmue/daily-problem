# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1, l2):
        result = None
        current_result_pointer = None
        current_l1 = l1
        current_l2 = l2
        carry = 0
        while current_l1 is not None or current_l2 is not None or carry:
            summand_1 = current_l1.val if current_l1 else 0
            summand_2 = current_l2.val if current_l2 else 0
            current_sum = (summand_1 + summand_2 + carry)
            carry = current_sum // 10
            current_sum %= 10
            if result is None:
                result = ListNode(current_sum)
                current_result_pointer = result
            else:
                current_result_pointer.next = ListNode(current_sum)
                current_result_pointer = current_result_pointer.next

            if current_l1 is not None:
                current_l1 = current_l1.next
            if current_l2 is not None:
                current_l2 = current_l2.next

        return result


l1 = ListNode(9)
l1.next = ListNode(9)
l1.next.next = ListNode(9)

l2 = ListNode(9)
l2.next = ListNode(9)
l2.next.next = ListNode(9)

result = Solution().addTwoNumbers(l1, l2)
while result is not None:
    print(result.val)
    result = result.next
