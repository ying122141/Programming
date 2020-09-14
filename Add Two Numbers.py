class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        carry = 0
        result = ListNode()
        mov_point = result
        
        while l1 or l2:
            x = (l1.val if l1 else 0)
            y = (l2.val if l2 else 0)
            
            carry, val = divmod(x + y + carry, 10)
            mov_point.next = ListNode(val)
            mov_point = mov_point.next
            
            l1 = (l1.next if l1 else None)
            l2 = (l2.next if l2 else None)
            
        if carry:
            mov_point.next = ListNode(1)
            
        return result.next